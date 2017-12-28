# -*- coding: utf-8 -*-
import unittest

from openprocurement.auctions.core.tests.base import snitch

from openprocurement.auctions.flash.tests.base import (
    BaseAuctionWebTest, test_bids, test_lots, test_organization
)
from openprocurement.auctions.flash.tests.blanks.award_blanks import (
    # AuctionAwardResourceTest
    create_auction_award_invalid,
    create_auction_award,
    patch_auction_award,
    patch_auction_award_unsuccessful,
    get_auction_award,
    patch_auction_award_Administrator_change,
    # AuctionLotAwardResourceTest
    create_auction_lot_award,
    patch_auction_lot_award,
    patch_auction_award_lot_unsuccessful,
    # Auction2LotAwardResourceTest
    create_auction_2_lot_award,
    patch_auction_2_award,
    # AuctionAwardComplaintResourceTest
    create_auction_award_complaint_invalid,
    create_auction_award_complaint,
    patch_auction_award_complaint,
    review_auction_award_complaint,
    get_auction_award_complaint,
    get_auction_award_complaints,
    # AuctionLotAwardComplaintResourceTest
    create_auction_lot_award_complaint,
    patch_auction_lot_award_complaint,
    get_auction_lot_award_complaint,
    get_auction_lot_award_complaints,
    # Auction2LotAwardComplaintResourceTest
    create_auction_2_lot_award_complaint,
    patch_auction_2_lot_award_complaint,
    # AuctionAwardComplaintDocumentResourceTest
    not_found_award_complaint_documen,
    create_auction_award_complaint_document,
    put_auction_award_complaint_document,
    patch_auction_award_complaint_document,
    # Auction2LotAwardComplaintDocumentResourceTest
    create_auction_award_2_lot_complaint_document,
    put_auction_award_2_lot_complaint_document,
    patch_auction_award_2_lot_complaint_document,
    # AuctionAwardDocumentResourceTest
    not_found_award_document_resource,
    create_auction_award_document,
    put_auction_award_document,
    patch_auction_award_document,
    create_auction_2_lot_award_document,
    put_auction_2_lot_award_document,
    patch_auction_2_lot_award_document
)


class AuctionAwardResourceTest(BaseAuctionWebTest):
    initial_status = 'active.qualification'
    initial_bids = test_bids
    test_create_auction_award_invalid = snitch(create_auction_award_invalid)
    test_create_auction_award = snitch(create_auction_award)
    test_patch_auction_award = snitch(patch_auction_award)
    test_patch_auction_award_unsuccessful = snitch(patch_auction_award_unsuccessful)
    test_get_auction_award = snitch(get_auction_award)
    test_patch_auction_award_Administrator_change = snitch(patch_auction_award_Administrator_change)


class AuctionLotAwardResourceTest(BaseAuctionWebTest):
    initial_status = 'active.qualification'
    initial_lots = test_lots
    initial_bids = test_bids
    test_create_auction_lot_award = snitch(create_auction_lot_award)
    test_patch_auction_lot_award = snitch(patch_auction_lot_award)
    test_patch_auction_award_lot_unsuccessful = snitch(patch_auction_award_lot_unsuccessful)


class Auction2LotAwardResourceTest(BaseAuctionWebTest):
    initial_status = 'active.qualification'
    initial_lots = 2 * test_lots
    initial_bids = test_bids
    test_create_auction_multiple_lot_award = snitch(create_auction_2_lot_award)
    test_patch_auction_multiple_award = snitch(patch_auction_2_award)


class AuctionAwardComplaintResourceTest(BaseAuctionWebTest):
    initial_status = 'active.qualification'
    initial_bids = test_bids

    def setUp(self):
        super(AuctionAwardComplaintResourceTest, self).setUp()
        # Create award
        response = self.app.post_json('/auctions/{}/awards'.format(
            self.auction_id),
            {'data': {'suppliers': [test_organization], 'status': 'pending', 'bid_id': self.initial_bids[0]['id']}})
        award = response.json['data']
        self.award_id = award['id']

    test_create_auction_award_complaint_invalid = snitch(create_auction_award_complaint_invalid)
    test_create_auction_award_complaint = snitch(create_auction_award_complaint)
    test_patch_auction_award_complaint = snitch(patch_auction_award_complaint)
    test_review_auction_award_complaint = snitch(review_auction_award_complaint)
    test_get_auction_award_complaint = snitch(get_auction_award_complaint)
    test_get_auction_award_complaints = snitch(get_auction_award_complaints)


class AuctionLotAwardComplaintResourceTest(BaseAuctionWebTest):
    initial_status = 'active.qualification'
    initial_lots = test_lots
    initial_bids = test_bids

    def setUp(self):
        super(AuctionLotAwardComplaintResourceTest, self).setUp()
        # Create award
        bid = self.initial_bids[0]
        response = self.app.post_json('/auctions/{}/awards'.format(
            self.auction_id), {'data': {'suppliers': [test_organization], 'status': 'pending', 'bid_id': bid['id'], 'lotID': bid['lotValues'][0]['relatedLot']}})
        award = response.json['data']
        self.award_id = award['id']
    test_create_auction_lot_award_complaint = snitch(create_auction_lot_award_complaint)
    test_patch_auction_lot_award_complaint = snitch(patch_auction_lot_award_complaint)
    test_get_auction_lot_award_complaint = snitch(get_auction_lot_award_complaint)
    test_get_auction_lot_award_complaints = snitch(get_auction_lot_award_complaints)


class Auction2LotAwardComplaintResourceTest(BaseAuctionWebTest):
    initial_status = 'active.qualification'
    initial_lots = 2 * test_lots
    initial_bids = test_bids

    def setUp(self):
        super(Auction2LotAwardComplaintResourceTest, self).setUp()
        # Create award
        bid = self.initial_bids[0]
        response = self.app.post_json('/auctions/{}/awards'.format(
            self.auction_id), {'data': {'suppliers': [test_organization], 'status': 'pending', 'bid_id': bid['id'], 'lotID': bid['lotValues'][0]['relatedLot']}})
        award = response.json['data']
        self.award_id = award['id']

    test_create_auction_2lot_award_complaint = snitch(create_auction_2_lot_award_complaint)
    test_patch_auction_2lot_award_complaint = snitch(patch_auction_2_lot_award_complaint)
    test_get_auction_lot_award_complaint = snitch(get_auction_lot_award_complaint)
    test_get_auction_lot_award_complaints = snitch(get_auction_lot_award_complaints)


class AuctionAwardComplaintDocumentResourceTest(BaseAuctionWebTest):
    initial_status = 'active.qualification'
    initial_bids = test_bids

    def setUp(self):
        super(AuctionAwardComplaintDocumentResourceTest, self).setUp()
        # Create award
        response = self.app.post_json('/auctions/{}/awards'.format(
            self.auction_id), {'data': {'suppliers': [test_organization], 'status': 'pending', 'bid_id': self.initial_bids[0]['id']}})
        award = response.json['data']
        self.award_id = award['id']
        # Create complaint for award
        response = self.app.post_json('/auctions/{}/awards/{}/complaints'.format(
            self.auction_id, self.award_id), {'data': {'title': 'complaint title', 'description': 'complaint description', 'author': test_organization}})
        complaint = response.json['data']
        self.complaint_id = complaint['id']
        self.complaint_owner_token = response.json['access']['token']
    test_not_found_award_complaint_documen = snitch(not_found_award_complaint_documen)
    test_create_auction_award_complaint_document = snitch(create_auction_award_complaint_document)
    test_put_auction_award_complaint_document = snitch(put_auction_award_complaint_document)
    test_patch_auction_award_complaint_document = snitch(patch_auction_award_complaint_document)


class Auction2LotAwardComplaintDocumentResourceTest(BaseAuctionWebTest):
    initial_status = 'active.qualification'
    initial_bids = test_bids
    initial_lots = 2 * test_lots

    def setUp(self):
        super(Auction2LotAwardComplaintDocumentResourceTest, self).setUp()
        # Create award
        bid = self.initial_bids[0]
        response = self.app.post_json('/auctions/{}/awards'.format(
            self.auction_id), {'data': {'suppliers': [test_organization], 'status': 'pending', 'bid_id': bid['id'], 'lotID': bid['lotValues'][0]['relatedLot']}})
        award = response.json['data']
        self.award_id = award['id']
        # Create complaint for award
        response = self.app.post_json('/auctions/{}/awards/{}/complaints'.format(
            self.auction_id, self.award_id), {'data': {'title': 'complaint title', 'description': 'complaint description', 'author': test_organization}})
        complaint = response.json['data']
        self.complaint_id = complaint['id']
        self.complaint_owner_token = response.json['access']['token']
    test_create_auction_award_2lot_complaint_document = snitch(create_auction_award_2_lot_complaint_document)
    test_put_auction_award_2lot_complaint_document = snitch(put_auction_award_2_lot_complaint_document)
    test_patch_auction_award_2lot_complaint_document = snitch(patch_auction_award_2_lot_complaint_document)


class AuctionAwardDocumentResourceTest(BaseAuctionWebTest):
    initial_status = 'active.qualification'
    initial_bids = test_bids

    def setUp(self):
        super(AuctionAwardDocumentResourceTest, self).setUp()
        # Create award
        response = self.app.post_json('/auctions/{}/awards'.format(
            self.auction_id), {'data': {'suppliers': [test_organization], 'status': 'pending', 'bid_id': self.initial_bids[0]['id']}})
        award = response.json['data']
        self.award_id = award['id']
    test_not_found_award_document_resource = snitch(not_found_award_document_resource)
    test_create_auction_award_document = snitch(create_auction_award_document)
    test_put_auction_award_document = snitch(put_auction_award_document)
    test_patch_auction_award_document = snitch(patch_auction_award_document)


class Auction2LotAwardDocumentResourceTest(BaseAuctionWebTest):
    initial_status = 'active.qualification'
    initial_bids = test_bids
    initial_lots = 2 * test_lots

    def setUp(self):
        super(Auction2LotAwardDocumentResourceTest, self).setUp()
        # Create award
        bid = self.initial_bids[0]
        response = self.app.post_json('/auctions/{}/awards'.format(
            self.auction_id), {'data': {'suppliers': [test_organization], 'status': 'pending', 'bid_id': bid['id'], 'lotID': bid['lotValues'][0]['relatedLot']}})
        award = response.json['data']
        self.award_id = award['id']
    test_create_auction_2lot_award_document = snitch(create_auction_2_lot_award_document)
    test_put_auction_2lot_award_document = snitch(put_auction_2_lot_award_document)
    test_patch_auction_2lot_award_document = snitch(patch_auction_2_lot_award_document)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(AuctionAwardResourceTest))
    suite.addTest(unittest.makeSuite(AuctionLotAwardResourceTest))
    suite.addTest(unittest.makeSuite(Auction2LotAwardResourceTest))
    suite.addTest(unittest.makeSuite(AuctionAwardComplaintResourceTest))
    suite.addTest(unittest.makeSuite(AuctionLotAwardComplaintResourceTest))
    suite.addTest(unittest.makeSuite(Auction2LotAwardComplaintResourceTest))
    suite.addTest(unittest.makeSuite(AuctionAwardComplaintDocumentResourceTest))
    suite.addTest(unittest.makeSuite(Auction2LotAwardComplaintDocumentResourceTest))
    suite.addTest(unittest.makeSuite(AuctionAwardDocumentResourceTest))
    suite.addTest(unittest.makeSuite(Auction2LotAwardDocumentResourceTest))
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
