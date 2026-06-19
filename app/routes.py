from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app import db
from app.models import List, Item

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET'])
def index():
    # Fetch all lists and their associated items
    todo_lists = List.query.order_by(List.list_position).all()
    return render_template('index.html', todo_lists=todo_lists)

@bp.route('/list', methods=['POST'])
def add_list():
    title = request.form.get('title')
    if title:
        new_list = List(title=title)
        db.session.add(new_list)
        db.session.commit()
    return redirect(url_for('main.index'))

@bp.route('/list/<int:list_id>/delete', methods=['POST'])
def delete_list(list_id):
    todo_list = List.query.get_or_404(list_id)
    db.session.delete(todo_list)
    db.session.commit()
    return redirect(url_for('main.index'))

@bp.route('/list/<int:list_id>/item', methods=['POST'])
def add_item(list_id):
    item_name = request.form.get('item_name')
    if item_name:
        new_item = Item(list_id=list_id, item_name=item_name)
        db.session.add(new_item)
        db.session.commit()
    return redirect(url_for('main.index'))

@bp.route('/item/<int:item_id>/toggle', methods=['POST'])
def toggle_item(item_id):
    item = Item.query.get_or_404(item_id)
    item.item_status = not item.item_status
    db.session.commit()
    return redirect(url_for('main.index'))

@bp.route('/item/<int:item_id>/delete', methods=['POST'])
def delete_item(item_id):
    item = Item.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('main.index'))

@bp.route('/reorder_lists', methods=['POST'])
def reorder_lists():
    data = request.get_json()
    for index, list_id in enumerate(data.get('order', [])):
        lst = List.query.get(list_id)
        if lst:
            lst.list_position = index
    db.session.commit()
    return jsonify({"status": "success"})

@bp.route('/list/<int:list_id>/reorder_items', methods=['POST'])
def reorder_items(list_id):
    data = request.get_json()
    for index, item_id in enumerate(data.get('order', [])):
        item = Item.query.get(item_id)
        if item and item.list_id == list_id:
            item.item_position = index
    db.session.commit()
    return jsonify({"status": "success"})