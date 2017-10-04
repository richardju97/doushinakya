//
//  ViewController.swift
//  Doushinakya
//
//  Created by Richard Ju on 9/30/17.
//  Copyright © 2017 Richard Ju. All rights reserved.
//

import Cocoa

class ViewController: NSViewController {

    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }

    override var representedObject: Any? {
        didSet {
        // Update the view, if already loaded.
        }
    }

    @IBOutlet weak var VerbDic: NSTextField!

    @IBOutlet weak var DispVerb: NSTextField!
    
    @IBAction func Submit(_ sender: NSButton) {
        DispVerb.stringValue = "Testing"
    }
}

