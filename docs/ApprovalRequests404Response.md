# ApprovalRequests404Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**param** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.approval_requests404_response import ApprovalRequests404Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApprovalRequests404Response from a JSON string
approval_requests404_response_instance = ApprovalRequests404Response.from_json(json)
# print the JSON string representation of the object
print(ApprovalRequests404Response.to_json())

# convert the object into a dict
approval_requests404_response_dict = approval_requests404_response_instance.to_dict()
# create an instance of ApprovalRequests404Response from a dict
approval_requests404_response_from_dict = ApprovalRequests404Response.from_dict(approval_requests404_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


