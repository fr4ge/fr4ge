# SPDX-FileCopyrightText: Chris Wilson <christopher.david.wilson@gmail.com>
#
# SPDX-License-Identifier: Apache-2.0 OR MIT

"""Tests for fr4ge.main."""

import pytest

from fr4ge import main


def test_main_prints_greeting(capsys: pytest.CaptureFixture[str]) -> None:
    """Verify that main prints the expected greeting."""
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello from fr4ge!\n"
