from flask_restful import Resource
from flask import jsonify, request, json
from config import STRIPE_API_KEY

import stripe

stripe.api_key = STRIPE_API_KEY


def calculate_order_amount_in_cents(items=[]):
    # Stripe accepts value in cents
    total = 0
    for item in items:
        total += (item.get("quantity") * item.get("price"))
    return total * 100


class StripeResource(Resource):
    def post(self):
        try:
            data = json.loads(request.data)
            total_amount_cents = calculate_order_amount_in_cents(data.get("orderedItems"))
            intent = stripe.PaymentIntent.create(
                amount=total_amount_cents,
                currency='usd'
            )
            return jsonify({
                'clientSecret': intent['client_secret'],
                'totalAmount': total_amount_cents / 100,
                'arrivalDate': data.get("arrivalDate"),
                'chefId': data.get("chefId"),
                'userId': data.get("userId")
            })
        except Exception as e:
            return jsonify(error=str(e)), 403
