import requests


after= '2022-10-17T00:00:00'
before= '2022-10-18T23:59:59'

cookiwp = 'wordpress_test_cookie=WP Cookie check; wordpress_logged_in_fd328de3b426bdd50635e86f9b37fd2e=namvenus|1667242308|BkE7iDKUFpqaj2RrDJN7NTmkK4jgd4ao6M4K4OSHqIT|9a1048763501491ddf4bc25d31b42ec7d7dcd005da244368f7c8f51d6c3a9c97; tk_ai=woo:rJsjpJplc9Ydz6SjSJS8OVNj; wp-settings-8=libraryContent=browse&amp;ampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampproduct_cat_tab=pop&amp;ampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampeditor=tinymce&amp;ampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampmfold=o&amp;ampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampadvImgDetails=show&amp;ampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampampmfold=o&amp;ampampampampampampampampampampampampampampampampampampampampampmfold=o; wp-settings-time-8=1666032709; woocommerce_items_in_cart=1; woocommerce_cart_hash=055a3716add69c6c5ff1d31c6e0ec53e; wp_woocommerce_session_fd328de3b426bdd50635e86f9b37fd2e=8||1666205611||1666202011||a3966fd8c3eee88ac12122690889ae7b'
xwp = '7b23f0e257'
headerwp = {'cookie' : cookiwp,
            'x-wp-nonce' : xwp}
reponse = requests.get('https://curilic.com/wp-json/wc-analytics/reports/performance-indicators?after='+ after + '&before=' + before + '&stats=revenue/total_sales,revenue/net_revenue,orders/orders_count,orders/avg_order_value,products/items_sold,revenue/refunds,coupons/orders_count,coupons/amount&_locale=user',headers=headerwp).json()

res =    reponse[0]['label'] + ': ' +  str(round(reponse[0]['value'],2)) + '\n'\
        + reponse[1]['label'] + ': ' +  str(round(reponse[1]['value'],2)) + '\n'\
        + reponse[2]['label'] + ': ' + str(round(reponse[2]['value'],2)) + '\n'\
        + reponse[3]['label'] + ': ' + str(round(reponse[3]['value'],2)) + '\n'\
        + reponse[4]['label'] + ': ' + str(round(reponse[4]['value'],2)) + '\n'\
        + reponse[5]['label'] + ': ' + str(round(reponse[5]['value'],2)) + '\n'\
        + reponse[6]['label'] + ': ' + str(round(reponse[6]['value'],2)) + '\n'\

print(res)
