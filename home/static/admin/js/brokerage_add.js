$(document).ready(function () {
  function hideAll() {
    $("div.field-asset, div.field-quantity, div.field-price, div.field-fees, div.field-total, div.field-origin_in_national_currency, div.field-origin_in_foreign_currency, div.field-for_purchase_exchange_sell, div.field-purchase_value, div.field-for_sale_exchange_purchase, div.field-sell_value").hide();
    $(".brokerage-dynamic-field").hide();
  }

  function showDeposit() {
    $("div.field-fees, div.field-total, div.field-origin_in_national_currency, div.field-origin_in_foreign_currency, div.field-for_purchase_exchange_sell, div.field-purchase_value").show();
  }

  function showWithdraw() {
    $("div.field-fees, div.field-total, div.field-origin_in_national_currency, div.field-origin_in_foreign_currency, div.field-for_sale_exchange_purchase, div.field-sell_value").show();
  }
  function showBuy() {
    $("div.field-asset, div.field-quantity, div.field-price, div.field-total, div.field-origin_in_national_currency, div.field-origin_in_foreign_currency, div.field-for_purchase_exchange_sell, div.field-purchase_value").show();
  }
  function showSell() {
    $("div.field-asset, div.field-quantity, div.field-price, div.field-total, div.field-origin_in_national_currency, div.field-origin_in_foreign_currency, div.field-for_sale_exchange_purchase, div.field-sell_value").show();
  }
  function showDividend() {
    $("div.field-asset, div.field-total, div.field-origin_in_foreign_currency, div.field-for_sale_exchange_purchase, div.field-sell_value").show();
  }
  function showTax() {
    $("div.field-asset, div.field-total, div.field-origin_in_foreign_currency, div.field-for_sale_exchange_purchase, div.field-sell_value").show();
  }
  function showInterest() {
    $("div.field-total, div.field-origin_in_foreign_currency").show();
  }
  function showOther() {
    $("div.field-asset, div.field-quantity, div.field-price, div.field-fees, div.field-total, div.field-origin_in_national_currency, div.field-origin_in_foreign_currency, div.field-for_purchase_exchange_sell, div.field-purchase_value, div.field-for_sale_exchange_purchase, div.field-sell_value").show();
  }


  $("#id_operation").change(function (e) {
    e.preventDefault();

    let selectedValue = $(this).val();

    hideAll();

    $(".brokerage-dynamic-field h2").html(selectedValue);
    $(".brokerage-dynamic-field").show();
    switch (selectedValue) {
      case "Deposit": showDeposit(); break;
      case "Withdraw": showWithdraw(); break;
      case "Buy": showBuy(); break;
      case "Sell": showSell(); break;
      case "Dividend": showDividend(); break;
      case "Tax Paid": showTax(); break;
      case "Interest": showInterest(); break;
      case "Other": showOther(); break;
      default:
        $(".brokerage-dynamic-field").hide();
        break;
    }
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
