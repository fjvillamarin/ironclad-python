# CommentMetadataModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**marked_up_message** | **str** |  | [optional] 
**added_participants** | [**List[UserModel]**](UserModel.md) |  | [optional] 
**replied_to** | [**CommentMetadataModelRepliedTo**](CommentMetadataModelRepliedTo.md) |  | [optional] 

## Example

```python
from openapi_client.models.comment_metadata_model import CommentMetadataModel

# TODO update the JSON string below
json = "{}"
# create an instance of CommentMetadataModel from a JSON string
comment_metadata_model_instance = CommentMetadataModel.from_json(json)
# print the JSON string representation of the object
print(CommentMetadataModel.to_json())

# convert the object into a dict
comment_metadata_model_dict = comment_metadata_model_instance.to_dict()
# create an instance of CommentMetadataModel from a dict
comment_metadata_model_from_dict = CommentMetadataModel.from_dict(comment_metadata_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


