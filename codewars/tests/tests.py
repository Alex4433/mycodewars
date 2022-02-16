class test:
    def describe(self, *args):
        pass

    @staticmethod
    def assert_equals(func, result, *args):
        if func == result:
            print('#Good')
        else:
            print('#Bad case', func, 'should return', result)
