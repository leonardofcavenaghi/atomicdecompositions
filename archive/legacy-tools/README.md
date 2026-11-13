# Legacy tools

These scripts preserve earlier development and catalogue-generation workflows. Use the maintained [`scripts/`](../../scripts/) and [contribution guide](../../CONTRIBUTING.md) for current commands. Historical scripts can rewrite source or catalogue files and retain their original path assumptions; they are not supported maintenance entry points.

## Python utilities

### Catalogue generators and injectors

| File |
|---|
| [append_fanography.py](python/append_fanography.py) |
| [generate_catalog.py](python/generate_catalog.py) |
| [generate_catalog_fast.py](python/generate_catalog_fast.py) |
| [generate_catalog_incremental.py](python/generate_catalog_incremental.py) |
| [generate_datatable.py](python/generate_datatable.py) |
| [inject_fanography.py](python/inject_fanography.py) |
| [restructure_catalog.py](python/restructure_catalog.py) |
| [resume_catalog.py](python/resume_catalog.py) |
| [write_markdown_from_cache.py](python/write_markdown_from_cache.py) |

### Input construction and search

| File |
|---|
| [append_presets.py](python/append_presets.py) |
| [fast_fano_gen.py](python/fast_fano_gen.py) |
| [find_100_examples.py](python/find_100_examples.py) |
| [find_fanos.py](python/find_fanos.py) |
| [generated_fano_cases.py](python/generated_fano_cases.py) |
| [make_100_cases.py](python/make_100_cases.py) |

### Exploratory calculations and diagnostics

| File |
|---|
| [generate_matrices.py](python/generate_matrices.py) |
| [hodge_pn.py](python/hodge_pn.py) |
| [test.py](python/test.py) |
| [test_examples.py](python/test_examples.py) |
| [test_examples2.py](python/test_examples2.py) |
| [test_hodge.py](python/test_hodge.py) |
| [test_matrices.py](python/test_matrices.py) |
| [test_matrices2.py](python/test_matrices2.py) |
| [test_parse_k.py](python/test_parse_k.py) |
| [test_quot.py](python/test_quot.py) |
| [test_script.py](python/test_script.py) |
| [verify_fanography.py](python/verify_fanography.py) |
| [wait_test.py](python/wait_test.py) |

### One-off source and cache migrations

| File |
|---|
| [add_hodge_dict.py](python/add_hodge_dict.py) |
| [clean_cards.py](python/clean_cards.py) |
| [clean_cards2.py](python/clean_cards2.py) |
| [clean_hodge.py](python/clean_hodge.py) |
| [clean_hodge2.py](python/clean_hodge2.py) |
| [clean_hodge_pn.py](python/clean_hodge_pn.py) |
| [fix_cache.py](python/fix_cache.py) |
| [fix_catalog_indent.py](python/fix_catalog_indent.py) |
| [fix_categories.py](python/fix_categories.py) |
| [fix_details.py](python/fix_details.py) |
| [fix_fano.py](python/fix_fano.py) |
| [fix_hodge_again.py](python/fix_hodge_again.py) |
| [fix_hodge_diamond.py](python/fix_hodge_diamond.py) |
| [fix_hodge_indent.py](python/fix_hodge_indent.py) |
| [fix_latex.py](python/fix_latex.py) |
| [fix_matrix.py](python/fix_matrix.py) |
| [fix_newlines.py](python/fix_newlines.py) |
| [fix_one_case.py](python/fix_one_case.py) |
| [fix_push.py](python/fix_push.py) |
| [mutate_cache.py](python/mutate_cache.py) |
| [patch.py](python/patch.py) |
| [patch2.py](python/patch2.py) |
| [patch3.py](python/patch3.py) |
| [patch4.py](python/patch4.py) |
| [patch5.py](python/patch5.py) |
| [patch_cache.py](python/patch_cache.py) |
| [patch_fano.py](python/patch_fano.py) |
| [patch_fast.py](python/patch_fast.py) |
| [patch_generator.py](python/patch_generator.py) |
| [patch_generator2.py](python/patch_generator2.py) |
| [patch_generator3.py](python/patch_generator3.py) |
| [patch_gui.py](python/patch_gui.py) |
| [patch_gui2.py](python/patch_gui2.py) |
| [patch_instructions.py](python/patch_instructions.py) |
| [patch_markdown.py](python/patch_markdown.py) |
| [patch_parse.py](python/patch_parse.py) |
| [patch_restructure.py](python/patch_restructure.py) |
| [patch_resume.py](python/patch_resume.py) |
| [patch_style.py](python/patch_style.py) |
| [patch_ux.py](python/patch_ux.py) |
| [replace_atoms.py](python/replace_atoms.py) |
| [replace_cards.py](python/replace_cards.py) |
| [rewrite.py](python/rewrite.py) |
| [seed_cache.py](python/seed_cache.py) |
| [update_generator.py](python/update_generator.py) |
| [update_popups.py](python/update_popups.py) |
| [update_scraped.py](python/update_scraped.py) |

## Browser diagnostics

| File |
|---|
| [test_puppeteer.js](browser/test_puppeteer.js) |
| [test_puppeteer2.js](browser/test_puppeteer2.js) |
| [test_puppeteer3.js](browser/test_puppeteer3.js) |
| [test_puppeteer4.js](browser/test_puppeteer4.js) |
| [test_puppeteer5.js](browser/test_puppeteer5.js) |
| [test_puppeteer6.js](browser/test_puppeteer6.js) |
| [test_width.js](browser/test_width.js) |

These browser probes were superseded by [`test_catalog_navigation.js`](../../scripts/test_catalog_navigation.js) and [`test_gui_controls.js`](../../scripts/test_gui_controls.js). Their screenshots and local browser outputs are generated artifacts and are not shipped with the source.
