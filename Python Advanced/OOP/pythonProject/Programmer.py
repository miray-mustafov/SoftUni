class Programmer:
    def __init__(self, name, language, skill):
        self.name = name
        self.language = language
        self.skill = skill

    def watch_course(self, course_name, language, skills_earned):
        if self.language != language:
            return f"{self.name} does not know {language}"
        else:
            self.skill+=skills_earned
            return f"{self.name} watched {course_name}"

    def change_language(self,new_language, skills_needed):
        if new_language == self.language:
            return f"{self.name} already knows {new_language}"
        elif skills_needed<=self.skill:
            result=f"{self.name} switched from {self.language} to {new_language}"
            self.language=new_language
            return result
        else:
            return f"{self.name} needs {skills_needed-self.skill} more skills"


programmer = Programmer("John", "Java", 50)
print(programmer.watch_course("Python Masterclass", "Python", 84))
print(programmer.change_language("Java", 30))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Java: zero to hero", "Java", 50))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Python Masterclass", "Python", 84))