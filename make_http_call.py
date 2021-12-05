import time
import test_generated_api
from pprint import pprint
from test_generated_api.api import test_api
from test_generated_api.model.error_response import ErrorResponse
from test_generated_api.model.some_params import SomeParams

# Defining the host is optional and defaults to http://127.0.0.1
# See configuration.py for a list of all supported configuration parameters.
configuration = test_generated_api.Configuration(
    host = "http://127.0.0.1:8000"
)



# Enter a context with an instance of the API client
with test_generated_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = test_api.TestApi(api_client)
    params =  SomeParams(someInt=5, someString="foo")

    try:
        # Make a test call
        api_response = api_instance.test_call(params=params)
        pprint(api_response)
    except test_generated_api.ApiException as e:
        print("Exception when calling TestApi->test_call: %s\n" % e)
