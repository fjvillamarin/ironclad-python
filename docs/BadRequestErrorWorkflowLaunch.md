# BadRequestErrorWorkflowLaunch



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | A unique code to identify why the workflow cannot be launched. | [readonly] 
**message** | **str** | A message indicating why the workflow cannot be launched. | [readonly] 
**param** | **str** | The required or expected parameter(s) that may be missing in order to launch the workflow. | [readonly] 

## Example

```python
from openapi_client.models.bad_request_error_workflow_launch import BadRequestErrorWorkflowLaunch

# TODO update the JSON string below
json = "{}"
# create an instance of BadRequestErrorWorkflowLaunch from a JSON string
bad_request_error_workflow_launch_instance = BadRequestErrorWorkflowLaunch.from_json(json)
# print the JSON string representation of the object
print(BadRequestErrorWorkflowLaunch.to_json())

# convert the object into a dict
bad_request_error_workflow_launch_dict = bad_request_error_workflow_launch_instance.to_dict()
# create an instance of BadRequestErrorWorkflowLaunch from a dict
bad_request_error_workflow_launch_from_dict = BadRequestErrorWorkflowLaunch.from_dict(bad_request_error_workflow_launch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


