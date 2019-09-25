from jinja2 import Markup
from flask import render_template,request,jsonify

from pyecharts import options as opts
from pyecharts.charts import Bar,Line

from app.charts import bp
import random
from random import randrange
from datetime import datetime
import time

def bar_base(name,subtitle) -> Bar:
	c = (
		Bar()
		.add_xaxis(["衬衣","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"])
		.add_yaxis("商家A",[random.randint(10,1000) for _ in range(6)])
		.add_yaxis("商家B",[random.randint(10,1000) for _ in range(6)])
		.set_global_opts(title_opts=opts.TitleOpts(title=name,subtitle=subtitle))
	)
	return c

def line_base(timeStr)->Line:
	line = (
		Line()
		.add_xaxis([timeStr])
		.add_yaxis(
			series_name="",
			y_axis=[randrange(50,80) for _ in range(0)]
		)
		.set_global_opts(
			title_opts=opts.TitleOpts("动态数据"),
			xaxis_opts=opts.AxisOpts(type_="value"),
            yaxis_opts=opts.AxisOpts(type_="value"),
		)
	)
	return line

@bp.route('/barIndex')
def barIndex():
    return render_template("charts/charts.html")

@bp.route('/lineChart')
def lineChart():
	t = time.localtime(time.time())
	idx = time.strftime("%Y %m %d %H:%M:%S", t)
	c = line_base(idx)
	return c.dump_options_with_quotes()


@bp.route('/lineDynamicData')
def lineDynamicData():
	t = time.localtime(time.time())
	idx = time.strftime("%Y %m %d %H:%M:%S", t)
	return jsonify({"name":idx,"value":randrange(50,80)})

@bp.route("/barChart")
def barChart():
    result = request.args
    name = result.get("name")
    subtitle = result.get("subtitle")
    c = bar_base(name, subtitle)

    return c.dump_options_with_quotes()