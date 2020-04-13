from flask import request, render_template, current_app
from flask_login import login_required
from .. import app
from ..models.user import Permission
from ..models.comment import Comment
from ..decorators import permission_required


@app.route("/moderate")
@login_required
@permission_required(Permission.MODERATE)
def moderate():
    page = request.args.get("page", 1, type=int)
    pagination = Comment.query.order_by(Comment.timestamp.desc()).paginate(
        page, per_page=current_app.config["APP_COMMENTS_PER_PAGE"],
        erro_out=False)
    comments = pagination.items
    return render_template("moderate.html", comments=comments, pagination=pagination, page=page)
