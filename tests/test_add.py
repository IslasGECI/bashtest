import subprocess

def test_add():
    assert_augend_plus_addend_equals_total(1, 1, 2)
    assert_augend_plus_addend_equals_total(2, 2, 4)
    assert_augend_plus_addend_equals_total(1, 2, 3)

def assert_augend_plus_addend_equals_total(augend, addend, total):
    bash_command = f"./src/add {augend} {addend}"
    output = int(subprocess.getoutput(bash_command))
    assert output == total
