DEPOSIT = "Deposit";
WITHDRAW = "Withdraw";
BUY = "Buy";
SELL = "Sell";
DIVIDEND = "Dividend";
// TAX_PAID = "Tax Paid";
INTEREST = "Interest";
OTHER = "Other";

$(document).ready(function () {
  function hideAll() {
    $("div.field-symbol, \
      div.field-quantity, \
      div.field-price, \
      div.field-fees, \
      div.field-total, \
      div.field-origin_in_national_currency, \
      div.field-origin_in_foreign_currency, \
      div.field-for_purchase_exchange_sell, \
      div.field-purchase_value, \
      div.field-for_sale_exchange_purchase, \
      div.field-sell_value"
    ).hide();
    $(".brokerage-dynamic-field").hide();
    $(".brokerage-dynamic-field").css("border-style", "none");
  }
  function manageDeposit() {
    $("div.field-fees, \
      div.field-total, \
      div.field-origin_in_national_currency, \
      div.field-origin_in_foreign_currency, \
      div.field-for_purchase_exchange_sell, \
      div.field-purchase_value"
    ).show();
    return "dodgerblue";
  }
  function manageWithdraw() {
    $("div.field-fees, \
      div.field-total, \
      div.field-for_sale_exchange_purchase, \
      div.field-sell_value"
    ).show();
    return "olivedrab";
  }
  function manageBuy() {
    $("div.field-symbol, \
      div.field-quantity, \
      div.field-price, \
      div.field-total, \
      div.field-for_purchase_exchange_sell, \
      div.field-purchase_value"
    ).show();
    return "green";
  }
  function manageSell() {
    $("div.field-symbol, \
      div.field-quantity, \
      div.field-price, \
      div.field-total, \
      div.field-for_sale_exchange_purchase, \
      div.field-sell_value"
    ).show();
    return "goldenrod";
  }
  function manageDividend() {
    $("div.field-symbol, \
      div.field-total, \
      div.field-for_sale_exchange_purchase, \
      div.field-sell_value"
    ).show();
    return "rebeccapurple";
  }
  // function manageTax() {
  //   $("div.field-symbol, div.field-total, div.field-origin_in_foreign_currency, div.field-for_sale_exchange_purchase, div.field-sell_value").show();
  //   return "red";
  // }
  function manageInterest() {
    $("div.field-total").show();
    return "gray";
  }
  function manageOther() {
    $("div.field-symbol, \
      div.field-quantity, \
      div.field-price, \
      div.field-fees, \
      div.field-total, \
      div.field-origin_in_national_currency, \
      div.field-origin_in_foreign_currency, \
      div.field-for_purchase_exchange_sell, \
      div.field-purchase_value, \
      div.field-for_sale_exchange_purchase, \
      div.field-sell_value"
    ).show();
    return "darkslategray";
  }


  function appendNotes() {
    // TODO: put a setting to modify link as user
    $("div.field-for_purchase_exchange_sell.field-purchase_value").append(
      '<a class="fst-italic" href="https://www.bcb.gov.br/estabilidadefinanceira/historicocotacoes" \
      target="_blank" rel="noopener noreferrer">\
      Pra compra, ver o valor do dólar no dia pelo site do banco central</a>'
    );
    $("div.field-for_sale_exchange_purchase.field-sell_value").append(
      '<a class="fst-italic" href="https://www.bcb.gov.br/estabilidadefinanceira/historicocotacoes" \
      target="_blank" rel="noopener noreferrer">\
      Pra dividendos, cotação deve ser o valor do último dia útil da primeira quinzena do mês anterior</a>'
    );

    $("div.field-profit").append(
      '<span class="fst-italic">Lucros isentos e não tributáveis, se abaixo de R$35.000,00</span>'
    );

    $("div.field-total").append(
      '<span class="fst-italic">Pra dividendos, será salvo automaticamente uma entrada de taxa de 30% sobre o valor</span>'
    );
  }


  function clearAll() {
    $("div.field-symbol input, \
      div.field-quantity input, \
      div.field-price input, \
      div.field-fees input, \
      div.field-total input, \
      div.field-origin_in_national_currency input, \
      div.field-origin_in_foreign_currency input, \
      div.field-for_purchase_exchange_sell input, \
      div.field-purchase_value input, \
      div.field-for_sale_exchange_purchase input, \
      div.field-sell_value input"
    ).val(null);
  }


  $("#id_operation").change(function (e) {
    e.preventDefault();

    let selectedValue = $(this).val();
    let borderColor = null;

    hideAll();
    clearAll();

    $(".brokerage-dynamic-field > h2").html(selectedValue);
    $(".brokerage-dynamic-field").show();
    $(".brokerage-dynamic-field").css("border-style", "groove");
    switch (selectedValue) {
      case DEPOSIT: borderColor = manageDeposit(); break;
      case WITHDRAW: borderColor = manageWithdraw(); break;
      case BUY: borderColor = manageBuy(); break;
      case SELL: borderColor = manageSell(); break;
      case DIVIDEND: borderColor = manageDividend(); break;
      // case TAX_PAID: borderColor = manageTax(); break;
      case INTEREST: borderColor = manageInterest(); break;
      case OTHER: borderColor = manageOther(); break;
      default:
        $(".brokerage-dynamic-field").hide();
        break;
    }
    $(".brokerage-dynamic-field > h2").css("background", borderColor);
    $(".brokerage-dynamic-field").css("border-color", borderColor);
  });


  function mathExchange(exchange) {
    let feesValueField = parseFloat($("div.field-fees input").val());
    let feesValue = isNaN(feesValueField) ? 0 : feesValueField;
    let totalValue = parseFloat($("div.field-total input").val());
    let result = ((exchange * totalValue) + feesValue).toFixed(2);
    return result;
  }


  // ============================ Exchange auto complete START ============================
  $("div.field-for_purchase_exchange_sell > input").change(function (e) {
    e.preventDefault();
    let exchangeSell = parseFloat($(this).val());
    $("div.field-purchase_value > input").val(mathExchange(exchangeSell));
  });

  $("div.field-for_sale_exchange_purchase > input").change(function (e) {
    e.preventDefault();
    let exchangeBuy = parseFloat($(this).val());
    $("div.field-sell_value > input").val(mathExchange(exchangeBuy));
  });
  // ============================ Exchange auto complete END ============================


  $("div.field-total input").change(function (e) {
    e.preventDefault();
    let selectedValue = $("#id_operation").val();
    // Deposit logic
    if (selectedValue === DEPOSIT) {
      let totalValue = parseFloat($(this).val());
      // Fill national value
      $("div.field-origin_in_national_currency > input").val(totalValue);
      $("div.field-origin_in_foreign_currency > input").val(0);
    }
  });

  $("div.field-quantity > input").change(function (e) {
    e.preventDefault();
    let selectedValue = $("#id_operation").val();
    // Buy logic
    if (selectedValue === BUY) {
      let price = parseFloat($("div.field-price input").val());
      let quantity = parseFloat($(this).val());
      let totalValue = price * quantity;
      console.log(price);
      console.log(quantity);
      console.log(totalValue);
      // Fill total value
      $("div.field-total input").val(totalValue);
    }
  });

  $("div.field-price input").change(function (e) {
    e.preventDefault();
    let selectedValue = $("#id_operation").val();
    // Buy logic
    if (selectedValue === BUY || selectedValue === SELL) {
      let price = parseFloat($(this).val());
      let quantity = parseFloat($("div.field-quantity > input").val());
      let totalValue = price * quantity;
      console.log(price);
      console.log(quantity);
      console.log(totalValue);
      // Fill total value
      $("div.field-total input").val(totalValue);
    }
  });


  // disable mousewheel on a input number field when in focus
  // (to prevent Chromium browsers change the value when scrolling)
  $("form").on("focus", "input[type=number]", function (e) {
    $(this).on("wheel.disableScroll", function (e) {
      e.preventDefault()
    })
  })

  hideAll();
  appendNotes();
});
