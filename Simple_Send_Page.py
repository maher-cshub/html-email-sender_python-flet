
from flet import *
import os
import shutil
from mail_sender import main
class Simple_Send_Page(UserControl):

    def __init__(self,page):
        super().__init__(self)

        self.file_path = ""
        ##FUNCTION
        def savefile(e: FilePickerResultEvent):
            if e.files:
                file_name = e.files[0].name
                file_path = e.files[0].path
                copy_path = os.path.join(os.getcwd(),f"uploads\{file_name}")
                shutil.copy(file_path,copy_path)
                self.file_path = copy_path

        def send_email(e):
            main(email_content.value,recipient_name_content.value,email_object_content.value,self.file_path)
            return 
        
        ##FILE PICKER
        file_picker = FilePicker(on_result=savefile)
        page.overlay.append(file_picker)

        ##EMAIL UI
        email_title = Text("Recipient Email")
        email_content = TextField(hint_text="test@gmail.com",prefix_icon=icons.EMAIL)
        email_object_title = Text("Email Object")
        email_object_content = TextField(hint_text="Application to your Job Offer",prefix_icon=icons.TITLE)
        email_file_title = Text("Email File")
        email_file_content = ElevatedButton("Select HTML File",icon=icons.FILE_UPLOAD,on_click=lambda _: file_picker.pick_files(allow_multiple=False,allowed_extensions=["html","htm"]))
        
        ##RECIPIENT UI
        recipient_name = Text("Recipient Name")
        recipient_name_content = TextField(hint_text="James Bond XD ",prefix_icon=icons.PERSON)
                                                                              

        self.content = Container(
            content=Column(
                controls=
                [
                    Column(
                        controls=
                        [
                            ResponsiveRow(
                                controls=
                                [
                                    email_title,    
                                    email_content
                                ],
                            ),
                            ResponsiveRow(
                                controls=
                                [
                                    recipient_name,
                                    recipient_name_content
                                ],
                            ), 
                            ResponsiveRow(
                                controls=
                                [ 
                                    email_object_title,
                                    email_object_content
                                        
                                ],
                            ),
                            ResponsiveRow(
                                controls=
                                [
                                    email_file_title,
                                    email_file_content
                                ], 
                            ), 
                        ],
                        height=500,
                        alignment=MainAxisAlignment.SPACE_EVENLY   
                    ),

                    Column(
                        controls=
                        [
                            ResponsiveRow(
                                controls=
                                [
                                    ElevatedButton(text="Send",icon=icons.SEND_ROUNDED,on_click=send_email),
                                    
                                ], 
                            ),   
                        ],
                    )
 
                ],
                alignment=MainAxisAlignment.SPACE_BETWEEN 
            ),
            height=600,
            margin=15
        )

    def build(self):
        return self.content