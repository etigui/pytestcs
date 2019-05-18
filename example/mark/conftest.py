import pytest

def pytest_addoption(parser):
    parser.addoption("--file", action="store", default="test6.txt", help="my option: test.txt or text2.txt")
    parser.addoption("--ofile", action="store", help="run all combinations")
    parser.addoption("--ss", action="store", help="run all combinations")


@pytest.fixture
def file(request):
    return request.config.getoption("--file")

@pytest.fixture
def ss(request):
    with open(request.config.getoption("--ss")) as f:
        content = f.readlines()
    return [x.strip().split() for x in content]

'''
@pytest.fixture
def open_file(request):
    fileName = request.config.getoption("--ofile")

    with open(fileName) as f:
        content = f.readlines()

    content = [x.strip().split() for x in content]
    request.parametrize("param1, param2, param3", content)



def get_data(xx):

	with open("test.txt") as f:
		content = f.readlines()
	content = 
	return content
'''
def pytest_generate_tests(metafunc):

    fileName = metafunc.config.getoption("--ofile")
    
    if "param1" in metafunc.fixturenames and "param2" in metafunc.fixturenames and "param3" in metafunc.fixturenames:

        with open(fileName) as f:
            content = f.readlines()

        content = [x.strip().split() for x in content]
        metafunc.parametrize("param1, param2, param3", content)

    '''
    print(f'xxxxxxxxxxxxxxxxxxxxxxxx: {metafunc}')
    if 'param1' in metafunc.fixturenames:
        print(f'sssssssssssssss: {metafunc.config.getoption("--all")}')
        if metafunc.config.getoption('--all'):
            end = 5
        else:
            end = 2
        metafunc.parametrize("param1", range(end))
    '''
