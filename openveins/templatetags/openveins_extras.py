from django import template


register = template.Library()


@register.simple_tag
def render_quote_card(quote):
    t = template.loader.get_template('quote_card.html')
    return t.render(template.Context({'quote':  quote}))
