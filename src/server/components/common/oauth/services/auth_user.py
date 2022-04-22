from django.core.exceptions import ValidationError


class AuthUserService:

	USER_MEDIA_FOLDER_NAME = 'user'
	IMAGE_MEDIA_FOLDER_NAME = 'image'

	AVATAR_FILE_SIZE_LIMIT = 2 * 1024 * 1024  # 2MB

	@classmethod
	def get_path_upload_avatar(cls, instance, file):
		"""
		Preparing the path to the user's avatar file 
		format: <media>/user/<user_id>/image/avatar_<timestamp>.png

		"""
		return f'{cls.USER_MEDIA_FOLDER_NAME}/{instance.id}/{cls.IMAGE_MEDIA_FOLDER_NAME}/{file}'
	
	@classmethod
	def validate_avatar_file_size(cls, file_obj):
		if file_obj.size > cls.AVATAR_FILE_SIZE_LIMIT:
			raise ValidationError("The maximum allowed avatar's file size is 2mb")
