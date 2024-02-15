from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date

Base = declarative_base()


class Stock(Base):
    __tablename__ = "stocks"
    id = Column(String, primary_key=True)
    name = Column(String)
    price = Column(String)
    price_change = Column(String)
    prev_close = Column(String)
    open = Column(String)
    bid = Column(String)
    ask = Column(String)
    days_range = Column(String)
    year_range = Column(String)
    volume = Column(String)
    avg_volume = Column(String)
    market_cap = Column(String)
    beta = Column(String)
    pe = Column(String)
    eps = Column(String)
    earnings_date = Column(String)
    dividend_and_yield = Column(String)
    ex_dividend_yield = Column(String)
    target_est = Column(String)

    def __repr__(self):
        return "<Stock(name='{}', price='{}', price_change='{}', prev_close='{}', open='{}', bid='{}', ask='{}', days_range='{}', year_range='{}', volume='{}', avg_volume='{}', market_cap='{}', beta='{}', pe='{}', eps='{}', earnings_date='{}', dividend_and_yield='{}', ex_dividend_yield='{}', target_est='{}')>"\
                .format(self.name, self.price, self.price_change, self.prev_close, self.open, self.bid, self.ask, self.days_range, self.year_range, self.volume, self.avg_volume, self.market_cap, self.beta, self.pe, self.eps, self.earnings_date, self.dividend_and_yield, self.ex_dividend_yield, self.target_est)
