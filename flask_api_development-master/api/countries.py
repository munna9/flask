from flask import request, jsonify, Blueprint
from api import dbhelper

country_api = Blueprint("country_api", __name__)


@country_api.route("/countrydetails", methods=["GET"])
def Get_All_Country_Details():
    sql = "select * from country_details order by country_id"
    data = dbhelper.GetData(sql)
    results = []

    for row in data:
        results.append({"id": row[0], "name": row[1]})

    return jsonify({"results": results})

@country_api.route("/countrydetails/<string:id>", methods=["GET"])
def Get_Country_Details_by_id(id):
    sql = "select * from country_details where country_id = '{}'".format(id)
    data = dbhelper.GetData(sql)
    results = []
    for row in data:
        results.append({"id": row[0], "name": row[1]})

    return jsonify({"results": results})