# DeprecatedCreateACommentOnAWorkflowRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creator** | [**CreatorEmailModel**](CreatorEmailModel.md) |  | 
**comment** | **str** | The comment text to add, accepts user mentions in the form of &lt;@user_id_or_email&gt;. | 
**add_users_to_workflow** | **bool** | Must be set to true if mentioning users who are not participants on the workflow. | [optional] 
**replied_to_activity_feed_message_id** | **str** | Use to specify the comment to reply to | [optional] 

## Example

```python
from openapi_client.models.deprecated_create_a_comment_on_a_workflow_request import DeprecatedCreateACommentOnAWorkflowRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeprecatedCreateACommentOnAWorkflowRequest from a JSON string
deprecated_create_a_comment_on_a_workflow_request_instance = DeprecatedCreateACommentOnAWorkflowRequest.from_json(json)
# print the JSON string representation of the object
print(DeprecatedCreateACommentOnAWorkflowRequest.to_json())

# convert the object into a dict
deprecated_create_a_comment_on_a_workflow_request_dict = deprecated_create_a_comment_on_a_workflow_request_instance.to_dict()
# create an instance of DeprecatedCreateACommentOnAWorkflowRequest from a dict
deprecated_create_a_comment_on_a_workflow_request_from_dict = DeprecatedCreateACommentOnAWorkflowRequest.from_dict(deprecated_create_a_comment_on_a_workflow_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


