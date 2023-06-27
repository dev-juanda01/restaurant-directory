const dom = document;

(() => {
  const $form = dom.querySelector(".form-new");
  const $elementsForm = $form.getElementsByTagName("p");

  for (let i = 0; i < $elementsForm.length; i++) {
    const $field = $elementsForm[i];

    $field.children[0].classList.add("form-label");
    $field.children[1].classList.add("form-control");
  }
})();
