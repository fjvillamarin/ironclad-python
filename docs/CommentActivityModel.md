# CommentActivityModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**CommentMetadataModel**](CommentMetadataModel.md) |  | [optional] 
**id** | **str** |  | 
**type** | **str** |  | 
**author** | [**ActivityAuthorModel**](ActivityAuthorModel.md) |  | 
**is_external** | **bool** |  | [optional] 
**reactions** | [**ActivityReactionModel**](ActivityReactionModel.md) |  | [optional] 

## Example

```python
from openapi_client.models.comment_activity_model import CommentActivityModel

# TODO update the JSON string below
json = "{}"
# create an instance of CommentActivityModel from a JSON string
comment_activity_model_instance = CommentActivityModel.from_json(json)
# print the JSON string representation of the object
print(CommentActivityModel.to_json())

# convert the object into a dict
comment_activity_model_dict = comment_activity_model_instance.to_dict()
# create an instance of CommentActivityModel from a dict
comment_activity_model_from_dict = CommentActivityModel.from_dict(comment_activity_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


