import SQLHelper
sql_helper = SQLHelper.connect(host="localhost", user="root", passwd="", db="first")
sql_helper.insert("first_note", idfirst_note="4", note_title="I am a boy",note_content="This is the article about a boy")
#INSERT INTO `first`.`first_note` (`idfirst_note`, `note_title`, `note_content`) VALUES ('0', 'hellp', 'helloworld');