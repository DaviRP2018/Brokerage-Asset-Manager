$(document).ready(function () {
  function hideAll() {
    $("div.field-asset, div.field-quantity, div.field-price, div.field-fees, div.field-total, div.field-origin_in_national_currency, div.field-origin_in_foreign_currency, div.field-for_purchase_exchange_sell, div.field-purchase_value, div.field-for_sale_exchange_purchase, div.field-sell_value").hide();
    $(".brokerage-dynamic-field").hide();
    $(".brokerage-dynamic-field").css("border-style", "none");
  }
  function manageDeposit() {
    $("div.field-fees, div.field-total, div.field-origin_in_national_currency, div.field-origin_in_foreign_currency, div.field-for_purchase_exchange_sell, div.field-purchase_value").show();
    return "dodgerblue";
  }
  function manageWithdraw() {
    $("div.field-fees, div.field-total, div.field-origin_in_national_currency, div.field-origin_in_foreign_currency, div.field-for_sale_exchange_purchase, div.field-sell_value").show();
    return "olivedrab";
  }
  function manageBuy() {
    $("div.field-asset, div.field-quantity, div.field-price, div.field-total, div.field-origin_in_national_currency, div.field-origin_in_foreign_currency, div.field-for_purchase_exchange_sell, div.field-purchase_value").show();
    return "green";
  }
  function manageSell() {
    $("div.field-asset, div.field-quantity, div.field-price, div.field-total, div.field-origin_in_national_currency, div.field-origin_in_foreign_currency, div.field-for_sale_exchange_purchase, div.field-sell_value").show();
    return "goldenrod";
  }
  function manageDividend() {
    $("div.field-asset, div.field-total, div.field-origin_in_foreign_currency, div.field-for_sale_exchange_purchase, div.field-sell_value").show();
    return "rebeccapurple";
  }
  function manageTax() {
    $("div.field-asset, div.field-total, div.field-origin_in_foreign_currency, div.field-for_sale_exchange_purchase, div.field-sell_value").show();
    return "red";
  }
  function manageInterest() {
    $("div.field-total, div.field-origin_in_foreign_currency").show();
    return "gray";
  }
  function manageOther() {
    $("div.field-asset, div.field-quantity, div.field-price, div.field-fees, div.field-total, div.field-origin_in_national_currency, div.field-origin_in_foreign_currency, div.field-for_purchase_exchange_sell, div.field-purchase_value, div.field-for_sale_exchange_purchase, div.field-sell_value").show();
    return "darkslategray";
  }


  $("#id_operation").change(function (e) {
    e.preventDefault();

    let selectedValue = $(this).val();
    let borderColor = null;

    hideAll();

    $(".brokerage-dynamic-field h2").html(selectedValue);
    $(".brokerage-dynamic-field").show();
    $(".brokerage-dynamic-field").css("border-style", "groove");
    switch (selectedValue) {
      case "Deposit": borderColor = manageDeposit(); break;
      case "Withdraw": borderColor = manageWithdraw(); break;
      case "Buy": borderColor = manageBuy(); break;
      case "Sell": borderColor = manageSell(); break;
      case "Dividend": borderColor = manageDividend(); break;
      case "Tax Paid": borderColor = manageTax(); break;
      case "Interest": borderColor = manageInterest(); break;
      case "Other": borderColor = manageOther(); break;
      default:
        $(".brokerage-dynamic-field").hide();
        break;
    }
    $(".brokerage-dynamic-field h2").css("background", borderColor);
    $(".brokerage-dynamic-field").css("border-color", borderColor);
  });


  hideAll();
  // TODO: put a setting to modify link as user
  $("div.field-for_purchase_exchange_sell.field-purchase_value").append(
    '<a class="fst-italic" href="https://www.bcb.gov.br/estabilidadefinanceira/historicocotacoes" target="_blank" rel="noopener noreferrer">Pra compra, ver o valor do dólar no dia pelo site do banco central</a>'
  );
  $("div.field-for_sale_exchange_purchase.field-sell_value").append(
    '<a class="fst-italic" href="https://www.bcb.gov.br/estabilidadefinanceira/historicocotacoes" target="_blank" rel="noopener noreferrer">Pra proventos, cotação deve ser o valor do último dia útil da primeira quinzena do mês anterior</a>'
  );

  $("div.field-profit").append(
    '<span class="fst-italic">Lucros isentos e não tributáveis, se abaixo de R$35.000,00</span>'
  );

});
