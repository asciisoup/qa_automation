def test_one(function_fixture, class_fixture, module_fixture, session_fixture):
    print("I\'m test_one NOT in test class one!")



def test_two(function_fixture, class_fixture, module_fixture, session_fixture):
    print("I\'m test_two NOT in test class two!")


class TestClass:
    def test_one(self, function_fixture, class_fixture, module_fixture, session_fixture):
        print("I\'m test_one in TestClass test class!")

    def test_two(self, function_fixture, class_fixture, module_fixture, session_fixture):
        print("I\'m test_two in TestClass test class!")


    def test_three(self, function_fixture, class_fixture, module_fixture, session_fixture):
        print("I\'m test_three in TestClass test class!")
