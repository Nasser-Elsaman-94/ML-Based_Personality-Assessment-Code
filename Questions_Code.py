from flask_wtf import FlaskForm
from wtforms import SubmitField, RadioField
from wtforms.validators import InputRequired


class DD_Form(FlaskForm):
    question1 = RadioField(
        'Are you the life of the party (Active person)? - هل أنت شخص نشيط للغاية؟',
        choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neutral'), (4, 'Agree'), (5, 'Strongly Agree')],
        validators=[InputRequired()]
    )

    question2 = RadioField(
        'Do you feel little concern for others? - هل تولّي إهتماماً قليلاً بالآخرين؟',
        choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neutral'), (4, 'Agree'), (5, 'Strongly Agree')],
        validators=[InputRequired()]
    )

    question3 = RadioField(
        'Are you always prepared? - هل دائماً تكون على استعداد لكل ما هو جديد؟',
        choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neutral'), (4, 'Agree'), (5, 'Strongly Agree')],
        validators=[InputRequired()]
    )

    question4 = RadioField(
        'Do you get stressed out easily? - هل تشعر بالتوتر بسهولة؟',
        choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neutral'), (4, 'Agree'), (5, 'Strongly Agree')],
        validators=[InputRequired()]
    )

    question5 = RadioField(
        "Do you have a rich vocabulary? - لديك حصيلة/ معرفة لغوية غنية بالمفردات والكلمات؟",
        choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neutral'), (4, 'Agree'), (5, 'Strongly Agree')],
        validators=[InputRequired()]
    )

    question6 = RadioField(
        "Do you not talk a lot? - لا تميل إلى التحدث كثيراً؟",
        choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neutral'), (4, 'Agree'), (5, 'Strongly Agree')],
        validators=[InputRequired()]
    )

    question7 = RadioField(
        "Are you interested in people? - تميل إلى الإهتمام بالآخرين ومساعدتهم؟",
        choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neutral'), (4, 'Agree'), (5, 'Strongly Agree')],
        validators=[InputRequired()]
    )

    question8 = RadioField(
        "Do you leave your belongings around? - تترك متعلقاتك الشخصية في أماكن متفرقة ولا تتذكرها كثيراً؟",
        choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neutral'), (4, 'Agree'), (5, 'Strongly Agree')],
        validators=[InputRequired()]
    )

    question9 = RadioField(
        "Are you relaxed most of the time? - تميل إلى الإسترخاء أغلب الوقت ولا تتحرك كثيراً؟",
        choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neutral'), (4, 'Agree'), (5, 'Strongly Agree')],
        validators=[InputRequired()]
    )

    question10 = RadioField(
        "Do you have difficulty understanding abstract ideas? - هل لديك القدرة على فهم الأفكار التجريدية والمفاهيم التصورية؟",
        choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neutral'), (4, 'Agree'), (5, 'Strongly Agree')],
        validators=[InputRequired()]
    )

    question11 = RadioField(
        "Do you feel comfortable around people? - هل تشعر بالراحة في التواجد حول الآخرين؟",
        choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neutral'), (4, 'Agree'), (5, 'Strongly Agree')],
        validators=[InputRequired()]
    )

    question12 = RadioField(
        "Do you insult people? - هل تحتقر الأشخاص الأدنى منك؟",
        choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neutral'), (4, 'Agree'), (5, 'Strongly Agree')],
        validators=[InputRequired()]
    )

    question13 = RadioField(
        "Do you pay attention to details? - هل تهتم بالتفاصيل؟",
        choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neutral'), (4, 'Agree'), (5, 'Strongly Agree')],
        validators=[InputRequired()]
    )

    question14 = RadioField(
        "Do you worry about things? - هل تقلق كثيراً من أبسط الأشياء؟",
        choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neutral'), (4, 'Agree'), (5, 'Strongly Agree')],
        validators=[InputRequired()]
    )

    question15 = RadioField(
        "Do you have a vivid imagination? - هل لديك خيال جامح؟",
        choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neutral'), (4, 'Agree'), (5, 'Strongly Agree')],
        validators=[InputRequired()]
    )

    question16 = RadioField(
        "Do you keep in the background? - أنت لا تُحِب الظهور كثيراً؟",
        choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neutral'), (4, 'Agree'), (5, 'Strongly Agree')],
        validators=[InputRequired()]
    )
    question17 = RadioField(
        "Do you sympathize with others' feelings? - هل تتعاطف مع مشاعر الآخرين؟",
        choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neutral'), (4, 'Agree'), (5, 'Strongly Agree')],
        validators=[InputRequired()]
    )

    question18 = RadioField(
        "Do you make a mess of things? - هل تميل إلى إحداث الفوضى في الأشياء؟",
        choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neutral'), (4, 'Agree'), (5, 'Strongly Agree')],
        validators=[InputRequired()]
    )

    question19 = RadioField(
        "Do you seldom feel blue? - نادراً ما تشعر بالكآبة والحزن؟",
        choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neutral'), (4, 'Agree'), (5, 'Strongly Agree')],
        validators=[InputRequired()]
    )

    question20 = RadioField(
        "Are you not interested in abstract ideas? - لا تهتم كثيراً بالأفكار التصورية والمفاهيم التجريدية؟",
        choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neutral'), (4, 'Agree'), (5, 'Strongly Agree')],
        validators=[InputRequired()]
    )
    question21 = RadioField(
        "Do you start conversations? - هل عادةً تبدأ المحادثات مع الآخرين؟",
        choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neutral'), (4, 'Agree'), (5, 'Strongly Agree')],
        validators=[InputRequired()]
    )

    question22 = RadioField(
        "Are you not interested in other people's problems? - هل لا تكترث ولا تهتم كثيراً بمشاكل الآخرين؟",
        choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neutral'), (4, 'Agree'), (5, 'Strongly Agree')],
        validators=[InputRequired()]
    )

    question23 = RadioField(
        "Do you get chores done right away? - هل تنجز أعمالك ومهامك المنزلية بسرعة؟",
        choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neutral'), (4, 'Agree'), (5, 'Strongly Agree')],
        validators=[InputRequired()]
    )

    question24 = RadioField(
        "Are you easily disturbed? - هل تغضب بسهولة وتنزعج من أبسط الأشياء؟",
        choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neutral'), (4, 'Agree'), (5, 'Strongly Agree')],
        validators=[InputRequired()]
    )

    question25 = RadioField(
        "Do you have excellent ideas? - هل لديك أفكار إبداعية ومميزة؟",
        choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neutral'), (4, 'Agree'), (5, 'Strongly Agree')],
        validators=[InputRequired()]
    )

    question26 = RadioField(
        "Do you have little to say? - هل تتحدث قليلاً؟",
        choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neutral'), (4, 'Agree'), (5, 'Strongly Agree')],
        validators=[InputRequired()]
    )

    question27 = RadioField(
        "Do you have a soft heart? - تتعامل برحمة ولين مع الأخرين؟",
        choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neutral'), (4, 'Agree'), (5, 'Strongly Agree')],
        validators=[InputRequired()]
    )

    question28 = RadioField(
        "Do you often forget to put things back in their proper place? - غالباً ما تنسى إعادة الأشياء في أماكنها الصحيحة؟",
        choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neutral'), (4, 'Agree'), (5, 'Strongly Agree')],
        validators=[InputRequired()]
    )

    question29 = RadioField(
        "Do you get upset easily? - هل تنزعج/ تتضايق بسهولة؟",
        choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neutral'), (4, 'Agree'), (5, 'Strongly Agree')],
        validators=[InputRequired()]
    )

    question30 = RadioField(
        "Do you not have a good imagination? - أنت لست واسع الخيال؟",
        choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neutral'), (4, 'Agree'), (5, 'Strongly Agree')],
        validators=[InputRequired()]
    )

    question31 = RadioField(
        "Do you talk to a lot of different people at parties? - يمكنك التحدث مع الغرباء دون الشعور بالإحراج؟",
        choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neutral'), (4, 'Agree'), (5, 'Strongly Agree')],
        validators=[InputRequired()]
    )

    question32 = RadioField(
        "Are you not really interested in others? - أنت لست مهتماً بالآخرين على الإطلاق؟",
        choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neutral'), (4, 'Agree'), (5, 'Strongly Agree')],
        validators=[InputRequired()]
    )

    question33 = RadioField(
        "Do you like order? - هل تُحِب النظام والترتيب؟",
        choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neutral'), (4, 'Agree'), (5, 'Strongly Agree')],
        validators=[InputRequired()]
    )

    question34 = RadioField(
        "Do you change your mood a lot? - هل أنت مُتَقلِب المزاج كثيراً؟",
        choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neutral'), (4, 'Agree'), (5, 'Strongly Agree')],
        validators=[InputRequired()]
    )

    question35 = RadioField(
        "Do you quick in understand things around you? - هل أنت سريع الفهم للأشياء من حولك؟",
        choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neutral'), (4, 'Agree'), (5, 'Strongly Agree')],
        validators=[InputRequired()]
    )

    question36 = RadioField(
        "Do you not like to draw attention to yourself? - أنت لا تُحِب أن تُلفِت الإنتباه إلى نفسك؟",
        choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neutral'), (4, 'Agree'), (5, 'Strongly Agree')],
        validators=[InputRequired()]
    )
    question37 = RadioField(
        "Do you take time out for others? - هل تمنح الآخرين جزءاً من وقتك لمساعدتهم؟",
        choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neutral'), (4, 'Agree'), (5, 'Strongly Agree')],
        validators=[InputRequired()]
    )

    question38 = RadioField(
        "Do you shirk your duties.? - هل تتهرب من واجباتك ومسؤولياتك؟",
        choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neutral'), (4, 'Agree'), (5, 'Strongly Agree')],
        validators=[InputRequired()]
    )

    question39 = RadioField(
        "Do you have frequent mood swings? - هل لديك تقلبات مزاجية متكررة؟",
        choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neutral'), (4, 'Agree'), (5, 'Strongly Agree')],
        validators=[InputRequired()]
    )
    question40 = RadioField(
        "Do you use difficult words? - هل تستخدم كلمات جزِلة/ صعبة؟",
        choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neutral'), (4, 'Agree'), (5, 'Strongly Agree')],
        validators=[InputRequired()]
    )

    question41 = RadioField(
        "Do you mind being the center of attention? - هل تمانع من أن تكون محط الأنظار؟",
        choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neutral'), (4, 'Agree'), (5, 'Strongly Agree')],
        validators=[InputRequired()]
    )

    question42 = RadioField(
        "Do you feel others' emotions? - هل تشعر بمشاعر الآخرين؟",
        choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neutral'), (4, 'Agree'), (5, 'Strongly Agree')],
        validators=[InputRequired()]
    )

    question43 = RadioField(
        "Do you follow a schedule? - هل تتبع جدولاً زمنياً معيناً؟",
        choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neutral'), (4, 'Agree'), (5, 'Strongly Agree')],
        validators=[InputRequired()]
    )

    question44 = RadioField(
        "Are you get irritated easily? - هل أنت سريع الغضب؟",
        choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neutral'), (4, 'Agree'), (5, 'Strongly Agree')],
        validators=[InputRequired()]
    )

    question45 = RadioField(
        "Do you spend time reflecting on things? - هل تقضي الوقت في التفكير وتحليل الأشياء والمواضيع؟",
        choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neutral'), (4, 'Agree'), (5, 'Strongly Agree')],
        validators=[InputRequired()]
    )

    question46 = RadioField(
        "Are you quiet around strangers? -هل تُجيد التحدث مع الغرباء؟",
        choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neutral'), (4, 'Agree'), (5, 'Strongly Agree')],
        validators=[InputRequired()]
    )
    question47 = RadioField(
        "Do make people feel at ease? -  هل تُشعِر الآخرين بالراحة وتعاملهم بالرفق واللين؟",
        choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neutral'), (4, 'Agree'), (5, 'Strongly Agree')],
        validators=[InputRequired()]
    )

    question48 = RadioField(
        "Are you exacting in my work? -  هل أنت صارمٌ في عملك؟",
        choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neutral'), (4, 'Agree'), (5, 'Strongly Agree')],
        validators=[InputRequired()]
    )

    question49 = RadioField(
        "Are you often feel blue? - هل كثيراً ماتشعر بالحزن؟",
        choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neutral'), (4, 'Agree'), (5, 'Strongly Agree')],
        validators=[InputRequired()]
    )

    question50 = RadioField(
        "Are you full of ideas? - هل لديك أفكار كثيرة إبداعية؟",
        choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neutral'), (4, 'Agree'), (5, 'Strongly Agree')],
        validators=[InputRequired()]
    )


    submit = SubmitField("Predict")
