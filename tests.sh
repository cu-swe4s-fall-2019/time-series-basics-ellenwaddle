test -e ssshtst || wget -qhttps://raw.githubusercontent.com/ryanlayer/ssshtest/mater/ssshtest
. ssshtst

run test_pycodestyle_di pycodestyle data_import.py
assert_exit_code 0

run test_pycodestyle_tdi pycodestyle test_data_import.py
assert_exit_code 0
