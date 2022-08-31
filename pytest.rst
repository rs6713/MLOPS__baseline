Pytest
======

Command Line
^^^^^^^^^^^^

-v verbose
pytest --show-capture=no



Mocking/Patching
^^^^^^^^^^^^^^^^^

Patch intercepts a call, returns a MagicMock object by default. By setting properties on MagicMock object, can mock call to return any value/raise an exception.
If you find yourself patching more than a handful of times, consider refactoring test/function you're testing.

> Patch where it is used, not where it is defined. Mock where it's imported to, not where imported from

**MagicMock**
^^^^^^^^^^^^^

Simple mocking itnerface to set reutrn val/behavior of function or object creation call you patched, without defining real object.

- **Return value** used to define what patched callable returns. When patching objects, the patched call is object creation, so return_value of the MagicMock could be another Mock object.

MagicMock flexibility can be a downside, by default acts like they have any attribute e.g. meant to mock a Response object, but actually patched afunction that returns request object.
Magicmock will still act like has properties request object. 

**Speccing**
Use spec keyword arg, creates MagicMock only with access to attrs/methods that are in teh class from which MagicMock specced.

MagicMock(spec=Response)

**Side Effect**

> Test function handles exception/ multiple calls of function you're patching correctly.
Set side_effect to an exception, to raise immediately when patched functioncalled.

mock_api_call.side_effect = SomeException()
mock_api_call.side_effect = [0, 1] # returns 0 first call, 1 on second.



Examples
^^^^^^^^

Assume functions/constants are defined in module2, but imported into module in the following examples.


**Constant**

.. code::
    with mock.patch("module.func.val", 2):
        ...
    @mock.patch("module.func.val", 2):
    def test_val():
        ...

**Functions**

Mocking methods works like mocking a funciton, just reference through class name: "moduel.classname.methodname"
Class static methods are the same as class methods.
@classmethod is the same as clas method, just return_value = class instance

.. code::
    @mock.patch("module.api_call")
    def test_some_func(self, mock_api_call):
        mock_api_call.return_value = MagicMock(status_code=200,response=json.dumps({'key':'value'}))

    @mock.patch("module.function1")
    @mock.patch("module.function2")
    def test_functions(self, function2, function1):
        function1.return_value = ...
        function2.return_value = ..

        function1.assert_called()
        function1.assert_called_once_with("baz")

        function1.call_count
        function1.called
        function1.call_args

**Properties**

Special methods on class with @property decorator

.. code::
    
    @mock.patch("module.classname.propertyname", new_callable=mock.PropertyMock)
    def test_property(self, mock_property):
        mock_property.return_value = 2

**Classes**

Return value should be new instance of mocked class.

.. code::
    @mock.patch("module.classname")
    def test_class(self, mock_class):

        class NewClass(object):
            def __init__():
                ..
        
        mock_class.return_value = NewClass()

**Decorators**

Defined at import time, thus difficult to redefine in mock. Better to create function for decorator body, and mock that.

**Context Mnagers**

@mock.patch("module.open_file")
def test_context_manager(self, mock_open_file):

    def enter_file(file):
        pass

    mock_open_file.return_value.__enter__ = enter_file

    mock_open_file.return_value.__enter__.return_value.name = "hi"

    # We enter the context manager instance
    with mock_open_file() as f:
        print(f.name)



Monkey Patching
^^^^^^^^^^^^^^^

> Dynamically changing a piece of software (module, object, method, function) at runtime.

Test out interfaces don't want to execute e.g. HTTP returns fixed data.
Decrease time for tests to execute.
Monkeypatching has a broader scope outside Tetsing, unlike mocking, though both are similar.

Pytest **monkeypatch** fixture, passed into function as an argument. Monkeypatching is only applied within function it is performed.
Here monkeypatching *os.getcwd()* call, simply return string. For more complex mocking, *monkeypatch.setattr(requests, "get", mock_get)*, have to define a function, that takes string and returns a mocked object class with status_code, url, headers attrs, and json(), __init__() methods.

.. code::

    def test_get_current_directory(monkeypatch):
        """
        GIVEN a monkeypatched version of os.getcwd()
        WHEN example1() is called
        THEN check the current directory returned
        """
        # Mock version of getcwd
        def mock_getcwd():
            return '/data/user/directory123'

        # Mock version called instead of original
        # Only applied within this test_ function
        monkeypatch.setattr(os, 'getcwd', mock_getcwd)
        assert example1() == '/data/user/directory123'

`Sources`
^^^^^^^^^
https://www.patricksoftwareblog.com/monkeypatching-with-pytest/
https://www.fugue.co/blog/2016-02-11-python-mocking-101