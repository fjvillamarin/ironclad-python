# CommentMetadataModelRepliedTo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_item** | **str** |  | [optional] 
**author** | [**ActivityAuthorModel**](ActivityAuthorModel.md) |  | [optional] 

## Example

```python
from openapi_client.models.comment_metadata_model_replied_to import CommentMetadataModelRepliedTo

# TODO update the JSON string below
json = "{}"
# create an instance of CommentMetadataModelRepliedTo from a JSON string
comment_metadata_model_replied_to_instance = CommentMetadataModelRepliedTo.from_json(json)
# print the JSON string representation of the object
print(CommentMetadataModelRepliedTo.to_json())

# convert the object into a dict
comment_metadata_model_replied_to_dict = comment_metadata_model_replied_to_instance.to_dict()
# create an instance of CommentMetadataModelRepliedTo from a dict
comment_metadata_model_replied_to_from_dict = CommentMetadataModelRepliedTo.from_dict(comment_metadata_model_replied_to_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


