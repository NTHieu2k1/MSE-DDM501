import joblib
import numpy as np
from .check_form import LoanCheckForm
from pathlib import Path

root_dir = Path(__file__).parent.parent
model_path = root_dir / 'models' / 'model.pkl'
model = joblib.load(model_path)
print('[INFO] Model loaded successfully.')


def convert_to_dict(form: LoanCheckForm):
    return {
        'name': form.name.data,
        'age': form.age.data,
        'gender': form.gender.data,
        'education': form.education.data,
        'income': form.income.data,
        'exp': form.exp.data,
        'home_ownership': form.home_ownership.data,
        'amount': form.amount.data,
        'intent': form.intent.data,
        'interest_rate': form.interest_rate.data,
        'credit_score': form.credit_score.data,
        'credit_hist_len': form.credit_hist_len.data,
        'prev_loan_default': form.prev_loan_default.data
    }


def make_record(data):
    label_str2int = {
        'gender': {'Female': 0, 'Male': 1},
        'education': {'High school': 0, 'Bachelor': 1, 'Master': 2, 'Doctorate': 3},
        'home_ownership': {'Rent': 0, 'Mortgage': 1, 'Own': 2, 'Other': 3},
        'intent': {'Education': 0, 'Medical': 1, 'Venture': 2, 'Personal': 3, 'Debt consolidation': 4,
                   'Home improvement': 5}
    }
    # Encode form inputs if needed & save to a record (for ML prediction)
    record = [
        data['age'],
        label_str2int['gender'][data['gender']],
        label_str2int['education'][data['education']],
        data['income'],
        data['exp'],
        label_str2int['home_ownership'][data['home_ownership']],
        data['amount'],
        label_str2int['intent'][data['intent']],
        data['interest_rate'],
        data['credit_score'],
        data['credit_hist_len'],
        int(data['prev_loan_default'])
    ]
    return np.expand_dims(record, axis=0)


def loan_approval_predict(data):
    record = make_record(data)
    pred_probs = model.predict_proba(record).squeeze()
    threshold = 0.5
    pred = 'Approved' if pred_probs[1] >= threshold else 'Rejected'
    confidence = pred_probs[1] if pred_probs[1] >= threshold else pred_probs[0]
    return pred, np.round(confidence, decimals=4)
