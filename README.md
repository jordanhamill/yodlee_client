# swagger-client
This file describes the Yodlee Platform APIs using the swagger notation. You can use this swagger file to generate client side SDKs to the Yodlee Platform APIs for many different programming languages. Yodlee supports the Java SDK and it is available <a href=\"https://developer.yodlee.com/java-sdk-overview \">here</a>. You can generate a client SDK for Python, Java, JavaScript, PHP, or other languages according to your development needs. For more details about the APIs, refer to <a href=\"https://developer.yodlee.com/docs/api/1.1/Overview\">Yodlee API v1.1 - Overview</a>.<br><br>You will have to set the header before making the API call. The following headers apply to all the APIs:<ul><li>Authorization: This header holds the access token</li> <li> Api-Version: 1.1</li></ul><b>Note</b>: If there are any API-specific headers, they are mentioned explicitly in the respective API's description.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.1.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import yodlee 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import yodlee
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import yodlee
from yodlee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = yodlee.AccountsApi(yodlee.ApiClient(configuration))
account_param = yodlee.CreateAccountRequest() # CreateAccountRequest | accountParam

try:
    # Add Manual Account
    api_response = api_instance.create_manual_account(account_param)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->create_manual_account: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountsApi* | [**create_manual_account**](docs/AccountsApi.md#create_manual_account) | **POST** /accounts | Add Manual Account
*AccountsApi* | [**delete_account**](docs/AccountsApi.md#delete_account) | **DELETE** /accounts/{accountId} | Delete Account
*AccountsApi* | [**evaluate_address**](docs/AccountsApi.md#evaluate_address) | **POST** /accounts/evaluateAddress | Evaluate Address
*AccountsApi* | [**get_account**](docs/AccountsApi.md#get_account) | **GET** /accounts/{accountId} | Get Account Details
*AccountsApi* | [**get_all_accounts**](docs/AccountsApi.md#get_all_accounts) | **GET** /accounts | Get Accounts
*AccountsApi* | [**get_associated_accounts**](docs/AccountsApi.md#get_associated_accounts) | **GET** /accounts/associatedAccounts/{providerAccountId} | Associated Accounts
*AccountsApi* | [**get_historical_balances**](docs/AccountsApi.md#get_historical_balances) | **GET** /accounts/historicalBalances | Get Historical Balances
*AccountsApi* | [**get_latest_balances**](docs/AccountsApi.md#get_latest_balances) | **GET** /accounts/latestBalances | Get Latest Balances
*AccountsApi* | [**migrate_accounts**](docs/AccountsApi.md#migrate_accounts) | **PUT** /accounts/migrateAccounts/{providerAccountId} | Migrate Accounts
*AccountsApi* | [**update_account**](docs/AccountsApi.md#update_account) | **PUT** /accounts/{accountId} | Update Account
*AuthApi* | [**delete_api_key**](docs/AuthApi.md#delete_api_key) | **DELETE** /auth/apiKey/{key} | Delete API Key
*AuthApi* | [**delete_token**](docs/AuthApi.md#delete_token) | **DELETE** /auth/token | Delete Token
*AuthApi* | [**generate_access_token**](docs/AuthApi.md#generate_access_token) | **POST** /auth/token | Generate Access Token
*AuthApi* | [**generate_api_key**](docs/AuthApi.md#generate_api_key) | **POST** /auth/apiKey | Generate API Key
*AuthApi* | [**get_api_keys**](docs/AuthApi.md#get_api_keys) | **GET** /auth/apiKey | Get API Keys
*CobrandApi* | [**cobrand_login**](docs/CobrandApi.md#cobrand_login) | **POST** /cobrand/login | Cobrand Login
*CobrandApi* | [**cobrand_logout**](docs/CobrandApi.md#cobrand_logout) | **POST** /cobrand/logout | Cobrand Logout
*CobrandApi* | [**create_subscription_event**](docs/CobrandApi.md#create_subscription_event) | **POST** /cobrand/config/notifications/events/{eventName} | Subscribe Event
*CobrandApi* | [**delete_subscribed_event**](docs/CobrandApi.md#delete_subscribed_event) | **DELETE** /cobrand/config/notifications/events/{eventName} | Delete Subscription
*CobrandApi* | [**get_public_key**](docs/CobrandApi.md#get_public_key) | **GET** /cobrand/publicKey | Get Public Key
*CobrandApi* | [**get_subscribed_events**](docs/CobrandApi.md#get_subscribed_events) | **GET** /cobrand/config/notifications/events | Get Subscribed Events
*CobrandApi* | [**update_subscribed_event**](docs/CobrandApi.md#update_subscribed_event) | **PUT** /cobrand/config/notifications/events/{eventName} | Update Subscription
*ConfigsApi* | [**create_subscription_notification_event**](docs/ConfigsApi.md#create_subscription_notification_event) | **POST** /configs/notifications/events/{eventName} | Subscribe For Notification Event
*ConfigsApi* | [**delete_subscribed_notification_event**](docs/ConfigsApi.md#delete_subscribed_notification_event) | **DELETE** /configs/notifications/events/{eventName} | Delete Notification Subscription
*ConfigsApi* | [**get_public_encryption_key**](docs/ConfigsApi.md#get_public_encryption_key) | **GET** /configs/publicKey | Get Public Key
*ConfigsApi* | [**get_subscribed_notification_events**](docs/ConfigsApi.md#get_subscribed_notification_events) | **GET** /configs/notifications/events | Get Subscribed Notification Events
*ConfigsApi* | [**update_subscribed_notification_event**](docs/ConfigsApi.md#update_subscribed_notification_event) | **PUT** /configs/notifications/events/{eventName} | Update Notification Subscription
*ConsentsApi* | [**create_consent**](docs/ConsentsApi.md#create_consent) | **POST** /consents | Post Consent
*ConsentsApi* | [**get_consent_details**](docs/ConsentsApi.md#get_consent_details) | **GET** /consents/{consentId} | Get Consent Details
*ConsentsApi* | [**get_consents**](docs/ConsentsApi.md#get_consents) | **GET** /consents | Get Consents
*ConsentsApi* | [**update_consent**](docs/ConsentsApi.md#update_consent) | **PUT** /consents/{consentId} | Put Consent
*DataExtractsApi* | [**get_data_extracts_events**](docs/DataExtractsApi.md#get_data_extracts_events) | **GET** /dataExtracts/events | Get Events
*DataExtractsApi* | [**get_data_extracts_user_data**](docs/DataExtractsApi.md#get_data_extracts_user_data) | **GET** /dataExtracts/userData | Get userData
*DerivedApi* | [**get_holding_summary**](docs/DerivedApi.md#get_holding_summary) | **GET** /derived/holdingSummary | Get Holding Summary
*DerivedApi* | [**get_networth**](docs/DerivedApi.md#get_networth) | **GET** /derived/networth | Get Networth Summary
*DerivedApi* | [**get_transaction_summary**](docs/DerivedApi.md#get_transaction_summary) | **GET** /derived/transactionSummary | Get Transaction Summary
*DocumentsApi* | [**delete_document**](docs/DocumentsApi.md#delete_document) | **DELETE** /documents/{documentId} | Delete Document
*DocumentsApi* | [**download_document**](docs/DocumentsApi.md#download_document) | **GET** /documents/{documentId} | Download a Document
*DocumentsApi* | [**get_documents**](docs/DocumentsApi.md#get_documents) | **GET** /documents | Get Documents
*EnrichDataApi* | [**push_user_data**](docs/EnrichDataApi.md#push_user_data) | **POST** /enrichData/userData | Push UserData
*HoldingsApi* | [**get_asset_classification_list**](docs/HoldingsApi.md#get_asset_classification_list) | **GET** /holdings/assetClassificationList | Get Asset Classification List
*HoldingsApi* | [**get_holding_type_list**](docs/HoldingsApi.md#get_holding_type_list) | **GET** /holdings/holdingTypeList | Get Holding Type List
*HoldingsApi* | [**get_holdings**](docs/HoldingsApi.md#get_holdings) | **GET** /holdings | Get Holdings
*HoldingsApi* | [**get_securities**](docs/HoldingsApi.md#get_securities) | **GET** /holdings/securities | Get Security Details
*InstitutionsApi* | [**get_institutions**](docs/InstitutionsApi.md#get_institutions) | **GET** /institutions | Get institutions
*ProviderAccountsApi* | [**delete_provider_account**](docs/ProviderAccountsApi.md#delete_provider_account) | **DELETE** /providerAccounts/{providerAccountId} | Delete Provider Account
*ProviderAccountsApi* | [**edit_credentials_or_refresh_provider_account**](docs/ProviderAccountsApi.md#edit_credentials_or_refresh_provider_account) | **PUT** /providerAccounts | Update Account
*ProviderAccountsApi* | [**get_all_provider_accounts**](docs/ProviderAccountsApi.md#get_all_provider_accounts) | **GET** /providerAccounts | Get Provider Accounts
*ProviderAccountsApi* | [**get_provider_account**](docs/ProviderAccountsApi.md#get_provider_account) | **GET** /providerAccounts/{providerAccountId} | Get Provider Account Details
*ProviderAccountsApi* | [**get_provider_account_profiles**](docs/ProviderAccountsApi.md#get_provider_account_profiles) | **GET** /providerAccounts/profile | Get User Profile Details
*ProviderAccountsApi* | [**link_provider_account**](docs/ProviderAccountsApi.md#link_provider_account) | **POST** /providerAccounts | Add Account
*ProviderAccountsApi* | [**update_preferences**](docs/ProviderAccountsApi.md#update_preferences) | **PUT** /providerAccounts/{providerAccountId}/preferences | Update Preferences
*ProvidersApi* | [**get_all_providers**](docs/ProvidersApi.md#get_all_providers) | **GET** /providers | Get Providers
*ProvidersApi* | [**get_provider**](docs/ProvidersApi.md#get_provider) | **GET** /providers/{providerId} | Get Provider Details
*ProvidersApi* | [**get_providers_count**](docs/ProvidersApi.md#get_providers_count) | **GET** /providers/count | Get Providers Count
*StatementsApi* | [**get_statements**](docs/StatementsApi.md#get_statements) | **GET** /statements | Get Statements
*TransactionsApi* | [**create_or_run_transaction_categorization_rules**](docs/TransactionsApi.md#create_or_run_transaction_categorization_rules) | **POST** /transactions/categories/rules | Create or Run Transaction Categorization Rule
*TransactionsApi* | [**create_transaction_category**](docs/TransactionsApi.md#create_transaction_category) | **POST** /transactions/categories | Create Category
*TransactionsApi* | [**delete_transaction_categorization_rule**](docs/TransactionsApi.md#delete_transaction_categorization_rule) | **DELETE** /transactions/categories/rules/{ruleId} | Delete Transaction Categorization Rule
*TransactionsApi* | [**delete_transaction_category**](docs/TransactionsApi.md#delete_transaction_category) | **DELETE** /transactions/categories/{categoryId} | Delete Category
*TransactionsApi* | [**get_transaction_categories**](docs/TransactionsApi.md#get_transaction_categories) | **GET** /transactions/categories | Get Transaction Category List
*TransactionsApi* | [**get_transaction_categorization_rules**](docs/TransactionsApi.md#get_transaction_categorization_rules) | **GET** /transactions/categories/txnRules | Get Transaction Categorization Rules
*TransactionsApi* | [**get_transaction_categorization_rules_deprecated**](docs/TransactionsApi.md#get_transaction_categorization_rules_deprecated) | **GET** /transactions/categories/rules | Get Transaction Categorization Rules
*TransactionsApi* | [**get_transactions**](docs/TransactionsApi.md#get_transactions) | **GET** /transactions | Get Transactions
*TransactionsApi* | [**get_transactions_count**](docs/TransactionsApi.md#get_transactions_count) | **GET** /transactions/count | Get Transactions Count
*TransactionsApi* | [**run_transaction_categorization_rule**](docs/TransactionsApi.md#run_transaction_categorization_rule) | **POST** /transactions/categories/rules/{ruleId} | Run Transaction Categorization Rule
*TransactionsApi* | [**update_transaction**](docs/TransactionsApi.md#update_transaction) | **PUT** /transactions/{transactionId} | Update Transaction
*TransactionsApi* | [**update_transaction_categorization_rule**](docs/TransactionsApi.md#update_transaction_categorization_rule) | **PUT** /transactions/categories/rules/{ruleId} | Update Transaction Categorization Rule
*TransactionsApi* | [**update_transaction_category**](docs/TransactionsApi.md#update_transaction_category) | **PUT** /transactions/categories | Update Category
*UserApi* | [**get_access_tokens**](docs/UserApi.md#get_access_tokens) | **GET** /user/accessTokens | Get Access Tokens
*UserApi* | [**get_user**](docs/UserApi.md#get_user) | **GET** /user | Get User Details
*UserApi* | [**register_user**](docs/UserApi.md#register_user) | **POST** /user/register | Register User
*UserApi* | [**saml_login**](docs/UserApi.md#saml_login) | **POST** /user/samlLogin | Saml Login
*UserApi* | [**unregister**](docs/UserApi.md#unregister) | **DELETE** /user/unregister | Delete User
*UserApi* | [**update_user**](docs/UserApi.md#update_user) | **PUT** /user | Update User Details
*UserApi* | [**user_logout**](docs/UserApi.md#user_logout) | **POST** /user/logout | User Logout
*VerificationApi* | [**get_verification_status**](docs/VerificationApi.md#get_verification_status) | **GET** /verification | Get Verification Status
*VerificationApi* | [**initiate_matching_or_challenge_deposite_verification**](docs/VerificationApi.md#initiate_matching_or_challenge_deposite_verification) | **POST** /verification | Initiaite Matching Service and Challenge Deposit
*VerificationApi* | [**verify_challenge_deposit**](docs/VerificationApi.md#verify_challenge_deposit) | **PUT** /verification | Verify Challenge Deposit
*VerifyAccountApi* | [**initiate_account_verification**](docs/VerifyAccountApi.md#initiate_account_verification) | **POST** /verifyAccount/{providerAccountId} | Verify Accounts Using Transactions


## Documentation For Models

 - [AccessTokens](docs/AccessTokens.md)
 - [Account](docs/Account.md)
 - [AccountAddress](docs/AccountAddress.md)
 - [AccountBalanceResponse](docs/AccountBalanceResponse.md)
 - [AccountDataset](docs/AccountDataset.md)
 - [AccountHistoricalBalancesResponse](docs/AccountHistoricalBalancesResponse.md)
 - [AccountHistory](docs/AccountHistory.md)
 - [AccountHolder](docs/AccountHolder.md)
 - [AccountLatestBalance](docs/AccountLatestBalance.md)
 - [AccountMigrationResponse](docs/AccountMigrationResponse.md)
 - [AccountProfile](docs/AccountProfile.md)
 - [AccountResponse](docs/AccountResponse.md)
 - [AddedProviderAccount](docs/AddedProviderAccount.md)
 - [AddedProviderAccountResponse](docs/AddedProviderAccountResponse.md)
 - [ApiKeyOutput](docs/ApiKeyOutput.md)
 - [ApiKeyRequest](docs/ApiKeyRequest.md)
 - [ApiKeyResponse](docs/ApiKeyResponse.md)
 - [AssetClassification](docs/AssetClassification.md)
 - [AssetClassificationList](docs/AssetClassificationList.md)
 - [AssociatedAccount](docs/AssociatedAccount.md)
 - [AssociatedAccountsResponse](docs/AssociatedAccountsResponse.md)
 - [Attribute](docs/Attribute.md)
 - [AutoRefresh](docs/AutoRefresh.md)
 - [BankTransferCode](docs/BankTransferCode.md)
 - [Capability](docs/Capability.md)
 - [ClientCredentialToken](docs/ClientCredentialToken.md)
 - [ClientCredentialTokenResponse](docs/ClientCredentialTokenResponse.md)
 - [Cobrand](docs/Cobrand.md)
 - [CobrandLoginRequest](docs/CobrandLoginRequest.md)
 - [CobrandLoginResponse](docs/CobrandLoginResponse.md)
 - [CobrandNotificationEvent](docs/CobrandNotificationEvent.md)
 - [CobrandNotificationResponse](docs/CobrandNotificationResponse.md)
 - [CobrandPublicKeyResponse](docs/CobrandPublicKeyResponse.md)
 - [CobrandSession](docs/CobrandSession.md)
 - [ConfigsNotificationEvent](docs/ConfigsNotificationEvent.md)
 - [ConfigsNotificationResponse](docs/ConfigsNotificationResponse.md)
 - [ConfigsPublicKey](docs/ConfigsPublicKey.md)
 - [ConfigsPublicKeyResponse](docs/ConfigsPublicKeyResponse.md)
 - [Consent](docs/Consent.md)
 - [ConsentResponse](docs/ConsentResponse.md)
 - [Contact](docs/Contact.md)
 - [ContainerAttributes](docs/ContainerAttributes.md)
 - [Coordinates](docs/Coordinates.md)
 - [Coverage](docs/Coverage.md)
 - [CoverageAmount](docs/CoverageAmount.md)
 - [CreateAccountInfo](docs/CreateAccountInfo.md)
 - [CreateAccountRequest](docs/CreateAccountRequest.md)
 - [CreateCobrandNotificationEvent](docs/CreateCobrandNotificationEvent.md)
 - [CreateCobrandNotificationEventRequest](docs/CreateCobrandNotificationEventRequest.md)
 - [CreateConfigsNotificationEvent](docs/CreateConfigsNotificationEvent.md)
 - [CreateConfigsNotificationEventRequest](docs/CreateConfigsNotificationEventRequest.md)
 - [CreateConsent](docs/CreateConsent.md)
 - [CreateConsentRequest](docs/CreateConsentRequest.md)
 - [CreatedAccountInfo](docs/CreatedAccountInfo.md)
 - [CreatedAccountResponse](docs/CreatedAccountResponse.md)
 - [CreatedConsentResponse](docs/CreatedConsentResponse.md)
 - [DataExtractsAccount](docs/DataExtractsAccount.md)
 - [DataExtractsEvent](docs/DataExtractsEvent.md)
 - [DataExtractsEventData](docs/DataExtractsEventData.md)
 - [DataExtractsEventLinks](docs/DataExtractsEventLinks.md)
 - [DataExtractsEventResponse](docs/DataExtractsEventResponse.md)
 - [DataExtractsEventUserData](docs/DataExtractsEventUserData.md)
 - [DataExtractsHolding](docs/DataExtractsHolding.md)
 - [DataExtractsProviderAccount](docs/DataExtractsProviderAccount.md)
 - [DataExtractsTransaction](docs/DataExtractsTransaction.md)
 - [DataExtractsUser](docs/DataExtractsUser.md)
 - [DataExtractsUserData](docs/DataExtractsUserData.md)
 - [DataExtractsUserDataResponse](docs/DataExtractsUserDataResponse.md)
 - [DerivedCategorySummary](docs/DerivedCategorySummary.md)
 - [DerivedCategorySummaryDetails](docs/DerivedCategorySummaryDetails.md)
 - [DerivedHolding](docs/DerivedHolding.md)
 - [DerivedHoldingSummaryResponse](docs/DerivedHoldingSummaryResponse.md)
 - [DerivedHoldingsAccount](docs/DerivedHoldingsAccount.md)
 - [DerivedHoldingsLinks](docs/DerivedHoldingsLinks.md)
 - [DerivedHoldingsSummary](docs/DerivedHoldingsSummary.md)
 - [DerivedNetworth](docs/DerivedNetworth.md)
 - [DerivedNetworthHistoricalBalance](docs/DerivedNetworthHistoricalBalance.md)
 - [DerivedNetworthResponse](docs/DerivedNetworthResponse.md)
 - [DerivedTransactionSummaryResponse](docs/DerivedTransactionSummaryResponse.md)
 - [DerivedTransactionsLinks](docs/DerivedTransactionsLinks.md)
 - [DerivedTransactionsSummary](docs/DerivedTransactionsSummary.md)
 - [Description](docs/Description.md)
 - [DetailCategory](docs/DetailCategory.md)
 - [Document](docs/Document.md)
 - [DocumentDownload](docs/DocumentDownload.md)
 - [DocumentDownloadResponse](docs/DocumentDownloadResponse.md)
 - [DocumentResponse](docs/DocumentResponse.md)
 - [Email](docs/Email.md)
 - [EnrichDataAccount](docs/EnrichDataAccount.md)
 - [EnrichDataRequest](docs/EnrichDataRequest.md)
 - [EnrichDataTransaction](docs/EnrichDataTransaction.md)
 - [EnrichDataUser](docs/EnrichDataUser.md)
 - [EnrichUserData](docs/EnrichUserData.md)
 - [EnrichedTransaction](docs/EnrichedTransaction.md)
 - [EnrichedTransactionResponse](docs/EnrichedTransactionResponse.md)
 - [EvaluateAccountAddress](docs/EvaluateAccountAddress.md)
 - [EvaluateAddressRequest](docs/EvaluateAddressRequest.md)
 - [EvaluateAddressResponse](docs/EvaluateAddressResponse.md)
 - [Field](docs/Field.md)
 - [FieldOperation](docs/FieldOperation.md)
 - [FullAccountNumberList](docs/FullAccountNumberList.md)
 - [HistoricalBalance](docs/HistoricalBalance.md)
 - [Holding](docs/Holding.md)
 - [HoldingAssetClassificationListResponse](docs/HoldingAssetClassificationListResponse.md)
 - [HoldingResponse](docs/HoldingResponse.md)
 - [HoldingSecuritiesResponse](docs/HoldingSecuritiesResponse.md)
 - [HoldingTypeListResponse](docs/HoldingTypeListResponse.md)
 - [Identifier](docs/Identifier.md)
 - [Institution](docs/Institution.md)
 - [InstitutionResponse](docs/InstitutionResponse.md)
 - [LoanPayoffDetails](docs/LoanPayoffDetails.md)
 - [LoginForm](docs/LoginForm.md)
 - [Merchant](docs/Merchant.md)
 - [Money](docs/Money.md)
 - [Name](docs/Name.md)
 - [Option](docs/Option.md)
 - [PaymentBankTransferCode](docs/PaymentBankTransferCode.md)
 - [PaymentIdentifier](docs/PaymentIdentifier.md)
 - [PaymentProfile](docs/PaymentProfile.md)
 - [PhoneNumber](docs/PhoneNumber.md)
 - [Profile](docs/Profile.md)
 - [ProviderAccount](docs/ProviderAccount.md)
 - [ProviderAccountDetail](docs/ProviderAccountDetail.md)
 - [ProviderAccountDetailResponse](docs/ProviderAccountDetailResponse.md)
 - [ProviderAccountPreferences](docs/ProviderAccountPreferences.md)
 - [ProviderAccountPreferencesRequest](docs/ProviderAccountPreferencesRequest.md)
 - [ProviderAccountProfile](docs/ProviderAccountProfile.md)
 - [ProviderAccountRequest](docs/ProviderAccountRequest.md)
 - [ProviderAccountResponse](docs/ProviderAccountResponse.md)
 - [ProviderAccountUserProfileResponse](docs/ProviderAccountUserProfileResponse.md)
 - [ProviderDetail](docs/ProviderDetail.md)
 - [ProviderDetailResponse](docs/ProviderDetailResponse.md)
 - [ProviderResponse](docs/ProviderResponse.md)
 - [Providers](docs/Providers.md)
 - [ProvidersCount](docs/ProvidersCount.md)
 - [ProvidersCountResponse](docs/ProvidersCountResponse.md)
 - [ProvidersDataset](docs/ProvidersDataset.md)
 - [RewardBalance](docs/RewardBalance.md)
 - [Row](docs/Row.md)
 - [RuleClause](docs/RuleClause.md)
 - [Scope](docs/Scope.md)
 - [Security](docs/Security.md)
 - [SecurityHolding](docs/SecurityHolding.md)
 - [Statement](docs/Statement.md)
 - [StatementResponse](docs/StatementResponse.md)
 - [StockExchangeDetail](docs/StockExchangeDetail.md)
 - [TotalCount](docs/TotalCount.md)
 - [Transaction](docs/Transaction.md)
 - [TransactionCategorizationRule](docs/TransactionCategorizationRule.md)
 - [TransactionCategorizationRuleInfo](docs/TransactionCategorizationRuleInfo.md)
 - [TransactionCategorizationRuleRequest](docs/TransactionCategorizationRuleRequest.md)
 - [TransactionCategorizationRuleResponse](docs/TransactionCategorizationRuleResponse.md)
 - [TransactionCategory](docs/TransactionCategory.md)
 - [TransactionCategoryRequest](docs/TransactionCategoryRequest.md)
 - [TransactionCategoryResponse](docs/TransactionCategoryResponse.md)
 - [TransactionCount](docs/TransactionCount.md)
 - [TransactionCountResponse](docs/TransactionCountResponse.md)
 - [TransactionDays](docs/TransactionDays.md)
 - [TransactionRequest](docs/TransactionRequest.md)
 - [TransactionResponse](docs/TransactionResponse.md)
 - [TransactionTotal](docs/TransactionTotal.md)
 - [UpdateAccountInfo](docs/UpdateAccountInfo.md)
 - [UpdateAccountRequest](docs/UpdateAccountRequest.md)
 - [UpdateCategoryRequest](docs/UpdateCategoryRequest.md)
 - [UpdateCobrandNotificationEvent](docs/UpdateCobrandNotificationEvent.md)
 - [UpdateCobrandNotificationEventRequest](docs/UpdateCobrandNotificationEventRequest.md)
 - [UpdateConfigsNotificationEvent](docs/UpdateConfigsNotificationEvent.md)
 - [UpdateConfigsNotificationEventRequest](docs/UpdateConfigsNotificationEventRequest.md)
 - [UpdateConsent](docs/UpdateConsent.md)
 - [UpdateConsentRequest](docs/UpdateConsentRequest.md)
 - [UpdateTransaction](docs/UpdateTransaction.md)
 - [UpdateUserRegistration](docs/UpdateUserRegistration.md)
 - [UpdateUserRequest](docs/UpdateUserRequest.md)
 - [UpdateVerification](docs/UpdateVerification.md)
 - [UpdateVerificationRequest](docs/UpdateVerificationRequest.md)
 - [UpdatedConsentResponse](docs/UpdatedConsentResponse.md)
 - [UpdatedProviderAccount](docs/UpdatedProviderAccount.md)
 - [UpdatedProviderAccountResponse](docs/UpdatedProviderAccountResponse.md)
 - [User](docs/User.md)
 - [UserAccessToken](docs/UserAccessToken.md)
 - [UserAccessTokensResponse](docs/UserAccessTokensResponse.md)
 - [UserAddress](docs/UserAddress.md)
 - [UserDetail](docs/UserDetail.md)
 - [UserDetailResponse](docs/UserDetailResponse.md)
 - [UserRegistration](docs/UserRegistration.md)
 - [UserRequest](docs/UserRequest.md)
 - [UserRequestPreferences](docs/UserRequestPreferences.md)
 - [UserResponse](docs/UserResponse.md)
 - [UserResponsePreferences](docs/UserResponsePreferences.md)
 - [UserSession](docs/UserSession.md)
 - [Verification](docs/Verification.md)
 - [VerificationAccount](docs/VerificationAccount.md)
 - [VerificationBankTransferCode](docs/VerificationBankTransferCode.md)
 - [VerificationRequest](docs/VerificationRequest.md)
 - [VerificationResponse](docs/VerificationResponse.md)
 - [VerificationStatus](docs/VerificationStatus.md)
 - [VerificationStatusResponse](docs/VerificationStatusResponse.md)
 - [VerificationTransaction](docs/VerificationTransaction.md)
 - [VerifiedAccount](docs/VerifiedAccount.md)
 - [VerifyAccount](docs/VerifyAccount.md)
 - [VerifyAccountRequest](docs/VerifyAccountRequest.md)
 - [VerifyAccountResponse](docs/VerifyAccountResponse.md)
 - [VerifyTransactionCriteria](docs/VerifyTransactionCriteria.md)
 - [YodleeError](docs/YodleeError.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author

developer@yodlee.com

