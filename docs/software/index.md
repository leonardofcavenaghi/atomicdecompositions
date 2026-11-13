---
description: Choose the combined flag and toric application or a individual distribution, with preserved original software and reproducible guides.
---

# Choose the software

Use the combined application to access flag and toric workspaces from one launcher. Separate launch modes remain available for users who need one geometry, and the original flag snapshot remains preserved.

Flag 1.0.6.dev0 and flag, toric and combined 1.1.0.dev1 are development distributions. The stable flag release remains v1.0.5.

| Distribution | Version | Interface | Guide |
|---|---|---|---|
| Combined flag and toric application | 1.1.0.dev1 | python -m gwapp; port 8650 | [Combined](combined.md) |
| Flag program 1.0.6.dev0 | 1.0.6.dev0 | python -m gwflags.gui; port 8642 | [Flags 1.0.6.dev0](flags-1.0.6.md) |
| Flag engine 1.1.0.dev1 | 1.1.0.dev1 | Standalone flag interface, or enhanced /flag/ workspace | [Flags 1.1.0.dev1](flags-1.1.0.md) |
| Toric engine 1.1.0.dev1 | 1.1.0.dev1 | python -m gwtoric.gui; port 8643 | [Toric varieties](toric-1.1.0.md) |
| Preserved original flag snapshot | 1.0.5 | Original flag interface and parameter names | [Archived guide](flags-legacy.md) |

The individual 1.1.0.dev1 distributions include shared flag and toric infrastructure needed by their execution tools. They omit the combined launcher; select the combined distribution for both workspaces. Install the flag versions in separate environments because they share the import name `gwflags`.

For a comparison of capabilities, read [Main changes](launch-2026-11.md), [Input/output conventions](input-output.md), and [Validation and reproducibility](launch-plan.md).

Start with [Installation](../installation.md). Read [Notation](notation.md) for parameter names, [Changes](changes.md) for the behavior changes, and [Releases](../releases.md) for the preserved stable download.

Existing catalog matrices retain their original ambient-node parameter names. Select the ambient compatibility convention to reproduce them; their coordinate conventions remain unchanged.

