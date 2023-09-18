"""
Base DexClient Class   🦄
"""


from typing import Optional

from loguru import logger
from web3 import Web3

from dxsp.utils import AccountUtils, ContractUtils


class DexClient:
    """
    Base DexClient Class

    Args:
        name (str): The name of the dex
        wallet_address (str): The wallet address
        private_key (str): The private key
        protocol_type (str): The protocol type
        protocol_version (int): The protocol version
        api_endpoint (str): The api endpoint
        api_key (str): The api key
        router_contract_addr (str): The router contract address
        factory_contract_addr (str): The factory contract address
        trading_asset_address (str): The trading asset address
        trading_risk_amount (int): The trading risk amount
        trading_slippage (int): The trading slippage
        block_explorer_url (str): The block explorer url
        block_explorer_api (str): The block explorer api
        w3 (Optional[Web3]): Web3


    """

    def __init__(
        self,
        name,
        wallet_address,
        private_key,
        protocol_type="uniswap",
        protocol_version=2,
        api_endpoint="https://api.0x.org/",
        api_key=None,
        router_contract_addr=None,
        factory_contract_addr=None,
        trading_asset_address=None,
        trading_slippage=None,
        trading_risk_amount=None,
        block_explorer_url="https://api.etherscan.io/api?",
        block_explorer_api=None,
        w3=None,
    ):
        self.w3 = w3
        self.name = name
        logger.debug(f"setting up DexClient: {self.name}")
        self.wallet_address = wallet_address
        self.private_key = private_key
        self.protocol_type = protocol_type
        self.protocol_version = protocol_version
        self.api_endpoint = api_endpoint
        self.api_key = api_key
        self.router_contract_addr = router_contract_addr
        self.factory_contract_addr = factory_contract_addr
        self.trading_asset_address = self.w3.to_checksum_address(trading_asset_address)
        self.trading_risk_amount = trading_risk_amount
        self.trading_slippage = trading_slippage
        self.block_explorer_url = block_explorer_url
        self.block_explorer_api = block_explorer_api

        self.account = AccountUtils(
            self.w3, self.wallet_address, self.private_key, self.trading_asset_address
        )
        self.contract_utils = ContractUtils(
            self.w3, self.block_explorer_url, self.block_explorer_api
        )

    async def get_quote(self, buy_address, sell_address, amount=1):
        """ """
        # return await self.dex_swap.get_quote(buy_address, sell_address, amount)

    async def get_swap(self, sell_address, buy_address, amount):
        """ """
        # return await self.dex_swap.get_swap(sell_address, buy_address, amount)

    async def get_info(self):
        """
        Get the information about the DexSwap API.

        Returns:
            str: A string containing the version of DexSwap, the name obtained from
                 `get_name()`, and the account number.
        Raises:
            Exception: If there is an error while retrieving the information.
        """
        try:
            return (
                f"💱 {self.name()}\n"
                # f"🪪 {self.account.account_number}"
            )
        except Exception as error:
            logger.error("info {}", error)

    async def get_account_balance(self):
        """
        Retrieves the account balance.

        :return: The account balance.
        :rtype: float
        """
        return await self.account.get_account_balance()

    async def get_trading_asset_balance(self):
        """
        Retrieves the trading asset balance for the current account.

        :return: A dictionary containing the trading asset balance.
                 The dictionary has the following keys:
                 - 'asset': The asset symbol.
                 - 'free': The free balance of the asset.
                 - 'locked': The locked balance of the asset.
        """
        return await self.account.get_trading_asset_balance()

    async def get_account_position(self):
        """
        Retrieves the account position.

        :return: The account position.
        :rtype: AccountPosition
        """
        return await self.account.get_account_position()

    async def get_account_margin(self):
        """
        Retrieves the account margin.

        :return: The account margin.
        :rtype: float
        """
        return await self.account.get_account_margin()

    async def get_account_open_positions(self):
        """
        Retrieves the open positions of the account.

        :return: A list of open positions in the account.
        """
        return await self.account.get_account_open_positions()

    async def get_account_transactions(self, period=24):
        """
        Get the account transactions
        for a specific period.

        Args:
            period (int): The number of hours
            for which to retrieve the transactions. Defaults to 24.

        Returns:
            List[Transaction]: A list of
            transaction objects representing the account transactions.
        """
        return await self.account.get_account_transactions(period)

    async def get_account_pnl(self, period=24):
        """
        Get the profit and loss (PnL)
        for the account within a specified period.

        Args:
            period (int, optional):
            The period in hours for which to calculate the PnL.
            Defaults to 24.

        Returns:
            float: The profit and loss (PnL)
            for the account within the specified period.
        """
        return await self.account.get_account_pnl(period)
