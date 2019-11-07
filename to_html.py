from search import search


def print_vocab(index, result, file=None):
    print("<tr class='post'>", file=file)
    print(f"<td id='{index}'>{index}</td>", file=file)
    print(
        f"<td class='font-weight-bold' onclick='toggle_visibility(this)' ><span class='invisible' id='invisible-title-{index}'>{result['title']}</span></td>",
        file=file,
    )
    print(f"<td><code>/{result['ipa']}/</code></td>", file=file)
    print(f"</tr>", file=file)
    for n, session in enumerate(result["sessions"]):
        for k, definition in enumerate(session[1][:3]):
            print("<tr class='align-text-bottom post'>", file=file)
            right = f"<span class='badge badge-info'>{session[0]}</span> <span class='font-weight-bold'>{definition[0]}</span>"
            left = ""
            for examples in definition[1]:
                left = f"{left}<br><span class='font-italic'>- {examples[0]}</span>"
                try:
                    right = f"{right}<br><span class='badge badge-warning'>例句</span> <span class='font-italic'>{examples[1]}</span>"
                except:
                    pass

            print(f"<td></td>", file=file)
            print(
                f"<td onclick='toggle_visibility(this)'><span id='invisible-{index}-{n}-{k}' class='invisible'>{left}</span></td>",
                file=file,
            )
            print(f"<td>{right}</td>", file=file)
            print("</tr>", file=file)


def head():
    return """<html>
<head>
  <meta charset="UTF-8">
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
    integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
</head>
<script src="https://unpkg.com/infinite-scroll@3/dist/infinite-scroll.pkgd.min.js"></script>
<style>
@font-face {
  /* Regular */
  font-family: "ConstructiumRegular";
  src: url("http://openfontlibrary.org/content/RebeccaRGB/412/Constructium.ttf") format("truetype");
  font-weight:  400;
  font-style:   normal;
  font-variant: normal;
  font-stretch: normal;
} 
</style>

<body class='container-fluid py-5'>
  <h1>Vocabulary 600</h1>
  <div class="">
    <table class='table table-bordered table-striped'>
      <thead class="thead-dark">
        <tr>
          <th scope="col">#</th>
          <th scope="col" width='48%'>Title</th>
          <th scope="col" width='48%'>Definition</th>
        </tr>
      </thead>
      <tbody class='content'>
  """


def bottom():
    return """
      </tbody>
    </div>
  </table>
</body>

<script>
  function toggle_visibility(e) {
    e.firstChild.classList.toggle('invisible')
  }
  var infScroll = new InfiniteScroll('.content', {
    onInit: function () {
      this.on('load', function () {
        console.log('Infinite Scroll load')
      });
    },
    path: function () {
      var pageNumber = (this.loadCount + 1);
      var path = './' + pageNumber + '.html'
      console.log('goto:', path)
      return path;
    },
    append: '.post',
    scrollThreshold: 100
  });

</script>

</html>
"""


if __name__ == "__main__":
    from json import dump
    from vocab import vocabs

    vocab_per_page = 10
    for i in range(0, 600, vocab_per_page):
        with open(f"vocabs/{int(i/vocab_per_page)}.html", "w", encoding="utf8") as f:
            print(head(), file=f)
            for n, vocab in enumerate(vocabs[i : i + vocab_per_page]):
                print(vocab)
                result = search(vocab)
                print_vocab((i + n + 1), result, file=f)
            print(bottom(), file=f)

