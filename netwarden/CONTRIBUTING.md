# Contributing to NetWarden

1. Create a branch from `main`: `feature/US-7-scan-diff` or `fix/42-ftp-banner`.
2. Write a failing test first, then the code. Keep commits small.
3. Run `ruff check src tests`, `mypy` and `pytest --cov` locally.
4. Use Conventional Commits: `feat(store): compare two scans (US-7)`, `fix(fingerprint): accept ProFTPD letter versions`.
5. Open a pull request. CI must pass and one reviewer must approve before merging (squash merge).

## Definition of done

* Acceptance criteria met and demonstrated.
* Tests added; coverage stays at or above 90%.
* Lint and type checks pass.
* Documentation and CHANGELOG updated.
* Reviewed and merged to `main`.
