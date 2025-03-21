# RevertToReviewRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**RevertToReviewRequestUser**](RevertToReviewRequestUser.md) |  | 

## Example

```python
from openapi_client.models.revert_to_review_request import RevertToReviewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RevertToReviewRequest from a JSON string
revert_to_review_request_instance = RevertToReviewRequest.from_json(json)
# print the JSON string representation of the object
print(RevertToReviewRequest.to_json())

# convert the object into a dict
revert_to_review_request_dict = revert_to_review_request_instance.to_dict()
# create an instance of RevertToReviewRequest from a dict
revert_to_review_request_from_dict = RevertToReviewRequest.from_dict(revert_to_review_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


