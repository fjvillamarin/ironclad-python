# ApprovalRequests200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] [default to 0]
**page_size** | **int** |  | [optional] [default to 20]
**count** | **int** |  | [optional] 
**list** | [**List[ApprovalRequests200ResponseListInner]**](ApprovalRequests200ResponseListInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.approval_requests200_response import ApprovalRequests200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApprovalRequests200Response from a JSON string
approval_requests200_response_instance = ApprovalRequests200Response.from_json(json)
# print the JSON string representation of the object
print(ApprovalRequests200Response.to_json())

# convert the object into a dict
approval_requests200_response_dict = approval_requests200_response_instance.to_dict()
# create an instance of ApprovalRequests200Response from a dict
approval_requests200_response_from_dict = ApprovalRequests200Response.from_dict(approval_requests200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


