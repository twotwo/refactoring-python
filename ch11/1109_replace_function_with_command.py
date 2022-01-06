"""
1109_replace_function_with_command.py

范例 下面的函数用于给一份保险申请评分
"""
# before
def score(candidate, medical_exam, scoring_guide):
    result = 0
    health_level = 0
    high_medical_risk_flag = False

    if medical_exam.is_smoker:
        health_level += 10
        high_medical_risk_flag = True

    certification_grade = "regular"

    if scoring_guide.stateWithLowCertification(candidate.originState):
        certification_grade = "low"
        result -= 5
    # lots more code like this
    result -= max(health_level - 5, 0)
    return result


# after
class Scorer:
    def __init__(self, candidate, medical_exam, scoring_guide):
        """在命令对象的构造函数中传入参数，而不让 execute 函数接收参数"""
        self._candidate = candidate
        self._medical_exam = medical_exam
        self._scoring_guide = scoring_guide

    def execute(self):
        self._result = 0
        self._health_level = 0
        self._high_medical_risk_flag = False

        self.score_smoking()
        self._certification_grade = "regular"

        if self._scoring_guide.stateWithLowCertification(self._candidate.originState):
            self._certification_grade = "low"
            self._result -= 5
        # lots more code like this
        self._result -= max(self._health_level - 5, 0)
        return self._result

    def score_smoking(self):
        if self._medical_exam.is_smoker:
            self._health_level += 10
            self._high_medical_risk_flag = True
