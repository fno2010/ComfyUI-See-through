# Upstream sources

This repository is a maintained fork of
[`jtydhr88/ComfyUI-See-through`](https://github.com/jtydhr88/ComfyUI-See-through).

## Base versions

| Component | Revision | Date |
|---|---|---|
| Node wrapper (fork base) | `98d754bf04f668647919ab750eccb0e0640faa81` (0.5.0) | 2026-08-19 |
| Vendored See-through | `df019de5129d6c4b406587a14c3501669441a783` | 2026-10-06 |

The vendored source is under `see-through/`. It is not a git submodule because
ComfyUI custom-node distribution is expected to be a self-contained directory.

## Local fork changes

- Renamed generic vendor packages to avoid collisions with other custom nodes:
  - `common/modules` -> `seethrough_modules`
  - `common/utils` -> `seethrough_utils`
  - `annotators` -> `seethrough_annotators`
- Removed the `sys.modules["utils"]` / `sys.modules["modules"]` save-and-restore
  hack from `nodes.py`; vendor imports now use the unique package names.
- Removed the global fake `pycocotools` module; `seethrough_utils.cv` treats it
  as optional and only errors when mask RLE helpers are called.
- Ported the current Node wrapper's Marigold progress-bar control and
  torchvision >= 0.23 interpolation compatibility onto upstream `df019de`.
- Kept upstream scheduler configuration and process-cuts fixes from
  `df019de` instead of the older vendored snapshot.

## Syncing upstream

The upstream project is tracked as the `official` git remote:

```bash
git fetch official
git log --oneline HEAD...official/main
```

When updating the vendored source, replace `see-through/` from the desired
`official/main` commit, then repeat the namespace/import transforms and the
Marigold compatibility patch. Do not blindly replace `nodes.py`; it contains
ComfyUI-specific model loading, NF4, and post-processing code.

Model weights are not part of this repository. They live under
`ComfyUI/models/SeeThrough/` and are downloaded on first use.
