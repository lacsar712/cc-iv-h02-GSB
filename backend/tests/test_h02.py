from h02_extra_trap import dirt_armed, gate
from h02_ui_trap import paint_form
from rules import judge


def test_writer_gate_open():
    assert gate("writer") is True


def test_reader_gate_closed():
    assert gate("reader") is False
    assert gate(None) is False
    assert gate("") is False


def test_form_only_for_writer():
    assert paint_form(True) is True
    assert paint_form(False) is False


def test_reject_leaves_no_dirt():
    assert dirt_armed() is False


def test_seed_verdicts_unchanged():
    assert judge(0.78)[0] == "合格"
    assert judge(0.61)[0] == "衰减"
