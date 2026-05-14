"""Smoke test: every module in the package imports cleanly."""


def test_imports_ac7renamer():
    import ac7renamer.ac7renamer  # noqa: F401


def test_imports_myrenamerdlg(qapp):
    import ac7renamer.myrenamerdlg  # noqa: F401


def test_imports_singlefiletab(qapp):
    import ac7renamer.singlefiletab  # noqa: F401


def test_imports_multifiletab(qapp):
    import ac7renamer.multifiletab  # noqa: F401


def test_imports_multifilemodel(qapp):
    import ac7renamer.multifilemodel  # noqa: F401


def test_imports_columns():
    import ac7renamer.columns  # noqa: F401
