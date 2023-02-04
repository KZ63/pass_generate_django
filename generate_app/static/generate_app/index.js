// CSRF対策
const getCookie = (name) => {
    if (document.cookie && document.cookie !== '') {
      for (const cookie of document.cookie.split(';')) {
        const [key, value] = cookie.trim().split('=')
        if (key === name) {
          return decodeURIComponent(value)
        }
      }
    }
  }
const csrftoken = getCookie('csrftoken')

function getPassword() {
    const elements = document.getElementsByName('radioBox');
    let v = '';
    for (let i = 0; i < elements.length; i++) {
        if (elements[i].checked) {
            v = elements[i].value;
        }
    }

    const body = new URLSearchParams();
    body.append('digit', v);

    const word_element = document.getElementsByName('wordradiobox');
    let word_list = [];
    for (let i = 0; i < word_element.length; i ++) {
        if (word_element[i].checked) {
            word_list.push(word_element[i].value)
        }
    }
    body.append('word', word_list);

    console.log(body);
    const url = '{% url "generate" %}'
    fetch('generate/', {
        method: 'POST',
        body: body,
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
            'X-CSRFToken': csrftoken,
        },
    })
    .then((response) => {
        return response.json()
    })
    .then((response) => {
        console.log(response.password_list);
        const passArea = document.getElementById('passwords');
        for(i = 0; i < response.password_list.length; i++) {
            const element = Object.assign(document.createElement('li'), {
                innerHTML: response.password_list[i]
            });
            passArea.appendChild(element);
        }
    })
    .catch((error) => {
        console.log(error);
    })
}