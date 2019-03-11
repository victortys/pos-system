from flask import render_template, url_for, redirect, flash, request, json, jsonify
from . import inventory
from forms import InventoryForm
from flask_login import login_required

from app import db
from ..models import Inventory, Serializer


@inventory.route('/save_item', methods=['GET', 'POST'])
@login_required
def save_item():
    """
    Add an item
    """
    form = InventoryForm()
    if request.method == 'POST':
        data = request.get_json()
        item = Inventory(form.pid.data, form.name.data, form.price.data, form.quantity.data)
        db.session.add(item)
        db.session.commit()
        return json.dumps(item.serialize()), 200

    if request.method == 'GET':
        return jsonify('Add a new item'), 200


@inventory.route("/show_items")
@login_required
def show_items():
    """
    Display all inventory
    """
    items = Inventory.query.all()
    return json.dumps(Inventory.serialize_list(items)), 200


@inventory.route("/update_item/<int:pid>", methods=['GET', 'POST'])
@login_required
def update_items(pid):
    """
    Update inventory
    """
    item = Inventory.query.get_or_404(pid)
    form = InventoryForm(obj=Inventory)

    # update changes
    item.name = form.name.data
    item.price = form.price.data
    item.quantity = form.quantity.data
    db.session.commit()

    return json.dumps(item.serialize()), 200


@inventory.route("/delete_item/<int:pid>", methods=['GET', 'POST'])
@login_required
def delete_items(pid):
    """
    Delete inventory
    """
    item = Inventory.query.get_or_404(pid)
    db.session.delete(item)
    db.session.commit()
    return jsonify("Item deleted"), 200




