---
layout: page
title: {{ title }}
{% if permalink %}permalink: {{ permalink }} {% endif %}
---

{{ content }}

{% if footer %}
{{ footer }}
{% endif %}
