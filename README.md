# witr for VX / Rez

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/vx-org/.github/main/profile/assets/vx-symbol-dark.svg">
  <img src="https://raw.githubusercontent.com/vx-org/.github/main/profile/assets/vx-symbol-light.svg" width="48" alt="VX symbol">
</picture>

Real runtime packages for [witr](https://github.com/pranshuparmar/witr), built
from the official v0.3.4 Windows, Linux and macOS x64/arm64 release payloads.
`recipe.json` pins all six upstream SHA-256 digests and commit
`7e46fa68151fd7c59fb7a0cf4247a9a0ac0fbb6e`. This repository packages upstream
releases; it does not fork or rebuild witr.

The shared [vx-rez-packages](https://github.com/vx-org/vx-rez-packages) builder
produces a directly extractable Rez repository in each `.rez.tar.zst` asset.
`witr/0.3.4/package.py` exposes `tools = ['witr']` and prepends
`{root}/payload/bin` to PATH. Target-specific `platform` and `arch` packages are
included alongside the runtime. The schema-v1 `index.json` selects assets by
tool, version, platform, architecture and target triple.

Each bundle includes the actual upstream Apache-2.0 LICENSE, third-party legal
texts collected from the pinned source archive, upstream provenance, manifest
and all-regular-files SHA-256 list. The Windows payload also retains its upstream
README. The package LICENSE was checked against the pinned upstream Git blob;
`metadata/THIRD_PARTY_NOTICES.txt` records the source archive URL and digest.

From the shared builder checkout, with this repository at `../witr`:

```bash
vx uv run --locked python -m tools.build_bundle --definition ../witr/recipe.json --triple x86_64-pc-windows-msvc --output-dir dist
```

By default the builder executes `witr --version` and checks the
pinned upstream commit on the matching native platform. Cross-packaging with
`--no-smoke-test` proves bundle structure and checksums only.

The release workflow pins the shared workflow and `tooling-ref` to the same
immutable builder commit. Pull requests and main pushes run the complete native
matrix. A `witr-0.3.4` tag can publish only after all six native builds and the
complete release index pass. It uploads a draft, downloads and verifies every
asset, and makes the verified draft public. Publication and installed VX
acceptance are separate gates.

Windows ARM uses the checksum-pinned published x64 VX bootstrap because VX 0.9.35 has no Windows ARM asset. The runtime smoke uses native ARM Python and the upstream ARM witr executable. This validates the witr package; it does not establish a native Windows ARM VX release.
