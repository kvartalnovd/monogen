from django.core.exceptions import ValidationError


class AuthUserService:

	USER_MEDIA_FOLDER_NAME = 'user'
	IMAGE_MEDIA_FOLDER_NAME = 'image'

	AVATAR_FILE_SIZE_LIMIT = 2 * 1024 * 1024  # 2MB

	@staticmethod
	def get_path_upload_avatar(instance, file):
		"""
		Preparing the path to the user's avatar file 
		format: <media>/user/<user_id>/image/avatar_<timestamp>.png

		"""
		return f'{AuthUserService.USER_MEDIA_FOLDER_NAME}/{instance.id}/{AuthUserService.IMAGE_MEDIA_FOLDER_NAME}/{file}'
	
	@staticmethod
	def validate_avatar_file_size(file_obj):
		if file_obj.size > AuthUserService.AVATAR_FILE_SIZE_LIMIT:
			raise ValidationError("The maximum allowed avatar's file size is 2mb")
