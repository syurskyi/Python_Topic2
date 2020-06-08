# Python Unit Testing
# unittest � Unit testing framework.
# Unittest supports test automation, sharing of setup and shutdown code for tests, aggregation of tests into collections, and independence of the tests from
# the reporting framework.
# 
# To achieve this, unittest supports some important concepts in an object-oriented way:
#
# 'test fixture': A test fixture represents the preparation needed to perform one or more tests, and any associate cleanup actions.
# This may involve, for example, creating temporary or proxy databases, directories, or starting a server process.
#
# 'test case': A test case is the individual unit of testing. It checks for a specific response to a particular set of inputs.
# unittest provides a base class, TestCase, which may be used to create new test cases.
#
# 'test suite': A test suite is a collection of test cases, test suites, or both.
# It is used to aggregate tests that should be executed together.
#
# 'test runner': A test runner is a component which orchestrates the execution of tests and provides the outcome to the user.
# The runner may use a graphical interface, a textual interface, or return a special value to indicate the results of executing the tests.
#

#
# Skipping tests and expected failures
# Unittest supports skipping individual test methods and even whole classes of tests.
# In addition, it supports marking a test as an �expected failure,� a test that is broken and will fail, but shouldn�t be counted as a failure on a
# TestResult.
#
 
#
# Skipping a test is simply a matter of using the skip() decorator or one of its conditional variants.
#

# 
# Basic skipping looks like this:
# 

c_ MyTestCase?.?

    @u__.skip("demonstrating skipping")

    ___ test_nothing
        fail("shouldn't happen")

    @u__.skipIf(mylib.__version__ < (1, 3),
                     "not supported in this library version")

    ___ test_format

        # Tests that work for only a certain version of the library.

        p..

    @u__.skipUnless(___.platform.startswith("win"), "requires Windows")

    ___ test_windows_support

        # windows specific testing code

        p..

#
# Classes can be skipped just like methods:
# 

@u__.skip("showing class skipping")

c_ MySkippedTestCase?.?
    ___ test_not_run

        p..

# 
# TestCase.setUp() can also skip the test.
# This is useful when a resource that needs to be set up is not available.
#

# 
# Expected failures use the expectedFailure() decorator.
# 

c_ ExpectedFailureTestCase?.?

    @u__.expectedFailure

    ___ test_fail
        aE..(1, 0, "broken")

# 
# It�s easy to roll your own skipping decorators by making a decorator that calls skip() on the test when it wants it to be skipped.
# This decorator skips the test unless the passed object has a certain attribute:
# 

___ skipUnlessHasattr(obj, attr

    __ hasattr(obj, attr
        r_ l___ func: func

    r_ u__.skip("{!r} doesn't have {!r}".f..(obj, attr))
 

#
# The following decorators implement test skipping and expected failures:
#
# @unittest.skip(reason): 
# Unconditionally skip the decorated test.
# reason should describe why the test is being skipped.
#
# @unittest.skipIf(condition, reason): 
# Skip the decorated test if condition is true.
#
# @unittest.skipUnless(condition, reason): 
# Skip the decorated test unless condition is true.
#
# @unittest.expectedFailure: 
# Mark the test as an expected failure.
# If the test fails it will be considered a success.
# If the test passes, it will be considered a failure.
#
# exception unittest.SkipTest(reason) 
# This exception is raised to skip a test. 
# Usually you can use TestCase.skipTest() or one of the skipping decorators instead of raising this directly.
# Skipped tests will not have setUp() or tearDown() run around them.
# Skipped classes will not have setUpClass() or tearDownClass() run.
# Skipped modules will not have setUpModule() or tearDownModule() run.
#