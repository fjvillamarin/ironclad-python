# RevertToReviewRequestUser

The Ironclad user reverting the workflow to the Review step. The user must be a participant on the workflow.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The Ironclad user&#39;s email address. | [optional] 
**type** | **str** | The mechanism of identifying the Ironclad user&#39;s account. | [optional] [default to 'email']

## Example

```python
from openapi_client.models.revert_to_review_request_user import RevertToReviewRequestUser

# TODO update the JSON string below
json = "{}"
# create an instance of RevertToReviewRequestUser from a JSON string
revert_to_review_request_user_instance = RevertToReviewRequestUser.from_json(json)
# print the JSON string representation of the object
print(RevertToReviewRequestUser.to_json())

# convert the object into a dict
revert_to_review_request_user_dict = revert_to_review_request_user_instance.to_dict()
# create an instance of RevertToReviewRequestUser from a dict
revert_to_review_request_user_from_dict = RevertToReviewRequestUser.from_dict(revert_to_review_request_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


