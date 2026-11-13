"""Exact, restartable sums over distinct unmarked decorations.

Persistent mode keeps canonical keys on disk and commits each batch of keys
together with its exact cumulative contribution. A killed worker loses only
the current transaction. No probabilistic hashes are used for deduplication.
"""
from fractions import Fraction
import json
from pathlib import Path
import sqlite3


class DecorationGroups:
    def __init__(self, path, width, batch_size=128):
        self.width=width;self.batch_size=batch_size;self.pending=0;self.count=0
        self.total=[Fraction(0)]*width;self.db=None;self.seen=set()
        if path is not None:
            path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
            self.db=sqlite3.connect(path)
            self.db.execute('PRAGMA journal_mode=WAL')
            self.db.execute('PRAGMA synchronous=FULL')
            self.db.execute('PRAGMA cache_size=-2048')
            self.db.execute('CREATE TABLE IF NOT EXISTS decorations (key TEXT PRIMARY KEY) WITHOUT ROWID')
            self.db.execute('CREATE TABLE IF NOT EXISTS progress (id INTEGER PRIMARY KEY CHECK(id=1), width INTEGER, count INTEGER, vals TEXT)')
            row=self.db.execute('SELECT width,count,vals FROM progress WHERE id=1').fetchone()
            if row:
                if row[0]!=width:raise ValueError('Decoration checkpoint width mismatch')
                self.count=row[1];self.total=[Fraction(v) for v in json.loads(row[2])]
                if len(self.total)!=width:raise ValueError('Decoration checkpoint values mismatch')
            else:
                self.db.execute('INSERT INTO progress VALUES(1,?,?,?)',(width,0,json.dumps(['0']*width)))
                self.db.commit()

    def contains(self, key):
        if self.db:
            return self.db.execute('SELECT 1 FROM decorations WHERE key=?',(key,)).fetchone() is not None
        return key in self.seen

    def add(self, key, values):
        if len(values)!=self.width:raise ValueError('Decoration contribution width mismatch')
        if self.db:self.db.execute('INSERT INTO decorations VALUES(?)',(key,))
        else:
            if key in self.seen:raise ValueError('Duplicate decoration')
            self.seen.add(key)
        self.total=[a+b for a,b in zip(self.total,values)]
        self.count+=1;self.pending+=1
        if self.pending>=self.batch_size:self.flush()

    def flush(self):
        if self.db and self.pending:
            self.db.execute('UPDATE progress SET count=?,vals=? WHERE id=1',
                            (self.count,json.dumps([str(v) for v in self.total])))
            self.db.commit()
        self.pending=0

    def __enter__(self):return self

    def __exit__(self, exc_type, exc, tb):
        try:
            if exc_type is None:self.flush()
            elif self.db:self.db.rollback()
        finally:
            if self.db:self.db.close()
