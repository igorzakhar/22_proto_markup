from staticjinja import make_site


index_data = {
    'title': 'Личный кабинет - kupimsami.ru',
    'current_region': 'Новосибирск',
    'regions': ['Кемерово', 'Омск', 'Томск'],
    'username': 'Леонид Федорович',
    'requests_href': 'requests.html'
}

requests_data = {
    'header': 'Заявки',
    'date_time': 'вчера, в 12:50',
    'request_text': '''60шт. ПК от 72-15 до ПК 21-15,
                    Криводановка, с доставкой.''',
    'request_name': 'Алексей',
    'page_views': '12'
}

testimonials = {
    'user_info': 'Кирилл, 29 лет, г.Барабинск',
    'comment': '''Бла-бла, мне помогло, все супер! Бла-бла, мне помогло,
                все супер! Бла-бла, мне помогло, все супер! Бла-бла,
                мне помогло, все супер! Бла-бла, мне помогло, все супер!'''
}

index_data.update(requests_data)
index_data.update(testimonials)
requests_data.update(index_data)

if __name__ == '__main__':
    site = make_site(
        outpath='static',
        contexts=[('index.html', index_data),
                  ('requests.html', requests_data)]
    )
    site.render()
